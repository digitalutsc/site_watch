"""
config_utils.py - A collection of functions for validating and formatting the configuration file.
This module contains logic for validating the configuration file and formatting the data in the configuration file whcih SiteWatch uses to run tests.
"""

from ruamel.yaml import YAML
from colorama import Fore
import logging
import os
import sys

logging = logging.getLogger(__name__)

def format_config(config: dict) -> dict:
    """ Return a formatted configuration dictionary with all keys and values lowercased, and all underscore- or hyphen-separated 
    keys replaced with space-separated keys. """
    formatted_config = {}
    for key, value in config.items():
        # Lowercase the key if it is a string
        key = key.lower() if isinstance(key, str) else key
        # Replace underscores and hyphens with spaces
        key = key.replace(" ", "_") if isinstance(key, str) else key
        # Add the key-value pair to the formatted config
        formatted_config[key] = value
    
    return formatted_config

def check_config(config: dict) -> None:
    """ Validate the data in the configuration and exit the program if any errors are found."""
    # The data input is mandatory. Data can come from a CSV file, an Excel file, or a Google Sheets URL. 
    # So, one and only one of the following keys must be present in the configuration:
    #   - csv
    #   - excel
    #   - google_sheets
    data_inputs = {"csv", "excel", "google_sheets"}
    present_inputs = [key for key in data_inputs if key in config]
    num_present_inputs = len(present_inputs)
    if num_present_inputs > 1:
        print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
        logging.error(f"Invalid data inputs in the configuration file: {present_inputs}. Only one of the following keys may be present: csv, excel, google_sheets")
        exit(127)
    elif num_present_inputs == 0:
        print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
        logging.error(f"No data inputs were specified in the configuration file. One of the following keys must be present: csv, excel, google_sheets")
        exit(127)

    # Next check the email information. If an email is specified, we need to check that the following keys are present under the email key:
    #   - sender_email (must be a string)
    #   - sender_name (must be a string)
    #   - recipient_emails (must be a list)
    if "email" in config:
        # The email key must be a dictionary
        if not isinstance(config["email"], dict):
            print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
            logging.error("The email key must be a dictionary.")
            exit(127)
        # Check if all required keys are present and of correct type
        required_email_keys = {"sender_email": str, "sender_name": str, "recipient_emails": list}
        for key, value_type in required_email_keys.items():
            if key not in config["email"] or not isinstance(config["email"][key], value_type):
                print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
                logging.error(f"The {key} key is missing or has an invalid value in the configuration file. The {key} key must be present under the email key and have a value of type {value_type}.")
                exit(127)

    # Next check if the key "delete_stale_files_after" is present and is an integer
    if "delete_stale_files_after" in config:
        if not isinstance(config["delete_stale_files_after"], int):
            print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
            logging.error("The delete_stale_files_after key must be an integer.")
            exit(127)
    else:
        # If the key is not present, set the default value to 30 days
        config["delete_stale_files_after"] = 30
    
def extract_config(filename: str) -> dict:
    """Extracts the configuration from the YAML file at <filename> and returns it as a dictionary. """
    # First check if the file exists
    if not os.path.exists(filename):
        print(Fore.RED, "Invalid configuration file path. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid configuration file path: {filename}")
        sys.exit(127)
    
    # Then check if the file is an yml/yaml file
    if not filename.lower().endswith(('.yml', '.yaml')):
        print(Fore.RED, "Invalid configuration file. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid configuration file: {filename}. The configuration file must be a YAML or YML file.")
        sys.exit(127)

    with open(filename, "r") as config_file:
        yaml = YAML(typ="safe")
        config = yaml.load(config_file)
    
    if not isinstance(config, dict):
        print(Fore.RED, "The configuration file is not properly formatted.", Fore.RESET)
        logging.error("The configuration file is not properly formatted.")
        exit(127)

    # Check the configuration for errors
    config = format_config(config)
    check_config(config)

    return config
