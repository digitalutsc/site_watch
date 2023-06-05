#!/usr/bin/python3

from datetime import datetime
from typing import Optional

import sys
from termcolor import colored
from ruamel.yaml import YAML

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

import csv
import logging

from rich.progress import track
from rich.console import Console
from rich.theme import Theme
import time
import os

from collection_count_test import CollectionCountTest
from facet_load_test import FacetLoadTest
import colorama
from colorama import Fore


logging.basicConfig(filename='logfile.txt', level=logging.DEBUG)

def print_help() -> None:
    """Prints the help message to the console. """
    print("Usage: python3 site_watch.py <config_file>")
    print("See the README for more information.")

def setup_logging() -> None:
    """Sets up the logging configuration and creates the site_config.log file if it does not already exist. """
    logging.basicConfig(filename='site_watch.log', level=logging.DEBUG)

def display_logo() -> None:
    """Read the ASCII logo from the logo.txt file and prints it to the console in yellow. """
    with open("logo.txt", "r") as f:
        logo = f.read()
    print(colored(logo, "yellow"))

def extract_config(filename: str) -> dict:
    """Extracts the configuration from the YAML file at <filename> and returns it as a dictionary. """
    with open(filename, "r") as config_file:
        yaml = YAML(typ="safe")
        config = yaml.load(config_file)
    return config

def get_webdriver(browser: str, driver_path: str) -> WebDriver:
    """Returns a headless webdriver instance corresponding to <browser> with the driver at <driver_path>, or None if the browser is invalid.
    
    Current supported browsers: Chrome, Firefox, Internet Explorer

    NOTE: This function exits the program if the browser is invalid.
    """
    if browser == "chrome":  
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        return webdriver.Chrome(options=options, executable_path=driver_path)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        return webdriver.Firefox(options=options, executable_path=driver_path)
    elif browser == "ie":
        options = webdriver.IeOptions()
        options.add_argument("--headless")
        return webdriver.Ie(options=options, executable_path=driver_path)
    else:
        print(colored("Invalid browser specified in config file. Please see log for more details.", "red"))
        logging.log(logging.ERROR, f"Invalid browser {browser} specified in config file. Currenly, the browsers supported are Chrome, Firefox, and Internet Explorer")
        sys.exit(127)

def extract_csv(filename: str) -> tuple[list[dict], list]:
    """Extracts the data from the CSV file at <filename> and returns it as a list of dictionaries along with the headers. """
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [{k.lower(): v.lower() for k, v in row.items()} for row in reader]
    return data, reader.fieldnames

def parse_arguments(arguments: list) -> str:
    """Parses the command line arguments and returns the path to the config file if it exists, or exit if it does not exist. 
    
    NOTE: This function exits the program if the number of arguments is invalid.
    """
    if len(arguments) != 2:
        print(colored("Invalid number of arguments. Please see log for more details.", "red"))
        logging.error(f"Invalid number of arguments. Expected 1, but got {len(arguments) - 1}")
        sys.exit(127)
    else:
        return arguments[1]
    
def check_config_file_exists(filename: str) -> None:
    """Returns True if the config file at <filename> exists, or exit if it does not exist. 
    
    NOTE: This function exits the program if the config file does not exist.
    """
    try:
        with open(filename, "r") as config_file:
            logging.info(f"Config file found at {filename}")
    except FileNotFoundError:
        print(colored("Config file not found. Please see log for more details.", "red"))
        logging.error(f"Config file not found at {filename}. Please make sure the file exists and try again.")
        sys.exit(127)

def check_csv_file_exists(filename: str) -> None:
    """Returns True if the CSV file at <filename> exists, or exit if it does not exist.

    NOTE: This function exits the program if the CSV file does not exist.
    """
    try:
        with open(filename, "r") as csv_file:
            logging.info(f"CSV file found at {filename}")
    except FileNotFoundError:
        print(colored("CSV file not found. Please see log for more details.", "red"))
        logging.error(f"CSV file not found at {filename}. Please make sure the file exists and try again." )
        sys.exit(127)

def config_to_dict(config_file: str) -> dict:
    """Checks the config file at <config_file> for validity and returns the config as a dictionary if it is valid, or exit if it is invalid.
    
    NOTE: This function exits the program if the config file is invalid.
    """
    check_config_file_exists(config_file)
    config = extract_config(config_file)

    # Check if the config file is a dictionary
    if not isinstance(config, dict):
        print(colored("Invalid config file. Please see log for more details.", "red"))
        logging.error("Invalid config file format. The file must consist of lines of key-value pairs.")
        sys.exit(127)
    
    supported_browsers = ["chrome", "firefox", "ie"]

    # Lowercase everything in the config dict
    config = {key.lower(): value.lower() for key, value in config.items()}
    # if "browser" not in config:
    #     print(colored("Invalid config file. Please see log for more details.", "red"))
    #     logging.error("Invalid config file. The config file must contain a browser field.")
    #     sys.exit(127)
    # elif config["browser"] not in supported_browsers:
    #     print(colored("Invalid config file. Please see log for more details.", "red"))
    #     logging.error(f"Invalid config file. The browser {config['browser']} is not supported. Currently, the browsers supported are Chrome, Firefox, and Internet Explorer.")
    #     sys.exit(127)
    # if "driver_path" not in config:
    #     print(colored("Invalid config file. Please see log for more details.", "red"))
    #     logging.error("Invalid config file. The config file must contain a driver_path field.")
    #     sys.exit(127)
    if "input_csv" not in config:
        print(colored("Invalid config file. Please see log for more details.", "red"))
        logging.error("Invalid config file. The config file must contain a input_csv field.")
        sys.exit(127)

    # Verify CSV file
    check_csv_file_exists(config["input_csv"])
    csv_data, csv_headers = extract_csv(config["input_csv"])
    check_csv_file(csv_data, csv_headers)

    if "output_csv" not in config:
        logging.info("No output_csv field found in config file. Using default output.csv")
        config["output_csv"] = "output.csv"
    # Check if the output CSV file exists. If not, create it.
    if not os.path.exists(config["output_csv"]):
        logging.info(f"output_csv file not found. Creating file at {config['output_csv']}")
        with open(config["output_csv"], "w") as output_csv_file:
            pass
    return config

def check_csv_file(csv_data: list[dict], csv_headers: list) -> None:
    """ Verifies the contents of the CSV file and exits the program if the CSV file is invalid. """
    suuported_test_types = ["availability_test", 
                            "facet_load_test", 
                            "collection_count_test", 
                            "openseadragon_load_test", 
                            "mirador_viewer_load_test", 
                            "ableplayer_transcript_test"]
    for i in track(range(len(csv_data)), description="Verifying CSV File..."):
        # Check if the length of the row is equal to the length of the headers
        if len(csv_data[i]) != len(csv_headers):
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. The number of columns in row {i + 1} does not match the number of headers.")
            sys.exit(127)
        
        # If any value in the row is None, change it to an empty string
        for key, value in csv_data[i].items():
            if value is None:
                csv_data[i][key] = ""

        # Lowercase all the keys in the dictionary
        csv_data[i] = {key.lower(): value.lower() for key, value in csv_data[i].items()}
        # Check if the CSV file contains the required fields
        if "url" not in csv_data[i]:
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. URL column is missing from row {i + 1}")
            sys.exit(127)
        if csv_data[i]["url"] == "":
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. URL column is empty in row {i + 1}")
            sys.exit(127)
        if "test type" not in csv_data[i]:
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Type column is missing from row {i + 1}")
            sys.exit(127)
        if csv_data[i]["test type"] not in suuported_test_types:
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Type column contains an invalid test type in row {i + 1}")
            sys.exit(127)
        
        # Check specific fields for specific test types
        # Facet Load Tests need a string input representing the facet name
        if csv_data[i]["test type"] == "facet_load_test" and "test input" not in csv_data[i]:
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Input column is missing from row {i + 1}")
            sys.exit(127)
        if csv_data[i]["test type"] == "facet_load_test" and csv_data[i]["test input"] == "":
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Input column is empty in row {i + 1}")
            sys.exit(127)
        
        # Collection Count Tests need an integer input representing the expected number of collections
        if csv_data[i]["test type"] == "collection_count_test" and "test input" not in csv_data[i]:
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Input column is missing from row {i + 1}")
            sys.exit(127)
        if csv_data[i]["test type"] == "collection_count_test" and csv_data[i]["test input"] == "":
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Input column is empty in row {i + 1}")
            sys.exit(127)

        # Mirador Viewer Load Tests need an integer input representing the expected number of thumbnails
        if csv_data[i]["test type"] == "mirador_viewer_load_test" and "test input" not in csv_data[i]:
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Input column is missing from row {i + 1}")
            sys.exit(127)
        if csv_data[i]["test type"] == "mirador_viewer_load_test" and csv_data[i]["test input"] == "":
            print(colored("Invalid CSV file. Please see log for more details.", "red"))
            logging.error(f"Invalid CSV file. Test Input column is empty in row {i + 1}")
            sys.exit(127)

def run_collection_count_test(csv_row: dict, csv_row_number: int, collection_count_test: CollectionCountTest) -> bool:
    """ Runs a Collection Count Test. """
    try:
        collection_count_test.run(csv_row["url"], csv_row["test input"])
    except ValueError:
        print(Fore.RED, f"Invalid test input on row {csv_row_number + 1}. Please see log for more details.")
        logging.error(f"Invalid test input on row {csv_row_number + 1}. The test input must be an integer.")
        return False
    except AssertionError as e:
        # Get the assertion error message
        error_message = str(e)
        print(Fore.RED, f"Collection Count Test failed on row {csv_row_number + 1}. Please see log for more details.")
        logging.error(f"Collection Count Test failed on row {csv_row_number + 1}. The expected number of collections was not found. {error_message}")
        return False
    except Exception as e:
        print(Fore.RED, f"Collection Count Test failed on row {csv_row_number + 1}. Please see log for more details.")
        logging.error(f"Collection Count Test failed on row {csv_row_number + 1}. {e}")
        return False
    else:
        print(Fore.GREEN, f"Collection Count Test passed on row {csv_row_number + 1}.")
        logging.info(f"Collection Count Test passed on row {csv_row_number + 1}.")
        return True
    
def run_facet_load_test(csv_row: dict, csv_row_number: int, facet_load_test: FacetLoadTest):
    pass


# Greetings to user
logging.info("SiteWatch has started.")
display_logo()

setup_logging()

# Parse command line arguments and extract the configuration file path
config_file = parse_arguments(sys.argv)

# Verify configuration file and produce a dictionary from it
config = config_to_dict(config_file)

# Produce a list of dictionaries from the CSV file
csv_data, csv_headers = extract_csv(config["input_csv"])


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
collection_count_test = CollectionCountTest(driver)
facet_load_test = FacetLoadTest(driver)
with open(config['output_csv'], 'w') as output_csv:
    csv_writer = csv.writer(output_csv)
    # Write the header
    csv_writer.writerow(csv_headers + ["test result", "total time"])
    for csv_row_number in track(range(len(csv_data)), description="Running Tests..."):
        test_result = None
        # Record the current time
        start_time = time.time()
        if csv_data[csv_row_number]['test type'] == 'collection_count_test':
            test_result = run_collection_count_test(csv_data[csv_row_number], csv_row_number, collection_count_test)
        elif csv_data[csv_row_number]['test type'] == 'facet_load_test':
            test_result = run_facet_load_test(csv_data[csv_row_number], csv_row_number, facet_load_test)
        # Record the time after the test has finished
        end_time = time.time()
        # Calculate the total time taken
        total_time = end_time - start_time
        # Convert the total time to a string
        total_time = str(total_time)
        
        if test_result is not None:
            # Write the entire row plus the test result and total time to the output CSV file
            csv_data[csv_row_number]['test result'] = "Passed" if test_result else "Failed"
            csv_data[csv_row_number]['total time'] = total_time
            csv_writer.writerow(list(csv_data[csv_row_number].values()))
  
