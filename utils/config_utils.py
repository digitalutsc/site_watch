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
    if "csv" not in config and "excel" not in config and "google_sheets" not in config:
        print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
        logging.error("No data input was specified in the configuration file. One of the following keys must be present: csv, excel, google_sheets")
        exit(127)
    elif "csv" in config and "excel" in config:
        print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
        logging.error("Both CSV and Excel data inputs were specified in the configuration file. Only one of the following keys may be present: csv, excel, google sheets")
        exit(127)
    elif "csv" in config and "google_sheets" in config:
        print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
        logging.error("Both CSV and Google Sheets data inputs were specified in the configuration file. Only one of the following keys may be present: csv, excel, google sheets")
        exit(127)
    elif "excel" in config and "google_sheets" in config:
        print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
        logging.error("Both Excel and Google Sheets data inputs were specified in the configuration file. Only one of the following keys may be present: csv, excel, google sheets")
        exit(127)

    # Next check the email information. If an email is specified, we need to check that the following keys are present under the email key:
    #   - sender_email
    #   - sender_name
    #   - recipient_emails (must be a list)
    if "email" in config:
        if "sender_email" not in config["email"]:
            print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
            logging.error("No sender email was specified in the configuration file. The sender_email key must be present under the email key.")
            exit(127)
        if "sender_name" not in config["email"]:
            print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
            logging.error("No sender name was specified in the configuration file. The sender_name key must be present under the email key.")
            exit(127)
        if "recipient_emails" not in config["email"]:
            print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
            logging.error("No recipient emails were specified in the configuration file. The recipient_emails key must be present under the email key.")
            exit(127)
        if not isinstance(config["email"]["recipient_emails"], list):
            print(Fore.RED, "There are errors in the configuration file. See log for more details.", Fore.RESET)
            logging.error("The recipient_emails key must be a list of email addresses.")
            exit(127)
    
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
