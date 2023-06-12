"""
csv_utils.py - A collection of utility functions for working with data inputs from various sources such as Google Sheets, Excel files, and CSV files.

This module provides functions for extracting CSV data from Google Sheets, converting CSV data to other formats,
and performing various operations on CSV data. It also includes utility functions for working with CSV files,
such as reading and writing CSV files, and handling CSV data in memory.
"""

import sys
import requests
import csv
import os
import logging
import openpyxl

from colorama import Fore
from io import StringIO
from rich.progress import track
import io

logging = logging.getLogger(__name__)

def extract_google_sheet(link: str) -> csv.DictReader:
    """ Extract a CSV from a Google Sheet at <link> and return a CSV DictReader object containing the CSV data."""
    # Extract the gid part from the link
    start_index = link.find('gid=') + 4  # Add 4 to skip 'gid='
    gid = link[start_index:]
    url_parts = link.split('/')
    url_parts[6] = 'export?gid=' + str(gid) + '&format=csv'
    csv_url = '/'.join(url_parts)
    response = requests.get(url=csv_url, allow_redirects=True)

    if response.status_code == 404:
        print(Fore.RED, "Invalid Google Sheets URL. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid Google Sheets URL: {link}")
        sys.exit(127)

    # Sheets that aren't publicly readable return a 302 and then a 200 with a bunch of HTML for humans to look at.
    if response.content.strip().startswith(b'<!doctype html'):
        print(Fore.RED, "Inaccessible Google Sheets URL. Please see the log for more details.", Fore.RESET)
        logging.error(f"The Google spreadsheet at {link} is not accessible. Please check its \"Share\" settings.")
        sys.exit(127)
    
    # Convert response content to proper CSV format
    decoded_content = response.content.decode('utf-8')
    # Return a DictReader object containing the CSV data
    return csv.DictReader(decoded_content.splitlines(), delimiter=',')

def extract_excel(input_excel_path) -> csv.DictReader:
    """Convert the Excel file at <input_excel_path> to a CSV file and return a DictReader object containing the CSV data."""
    # First check if the file exists
    if not os.path.exists(input_excel_path):
        print(Fore.RED, "Invalid Excel file path. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid Excel file path: {input_excel_path}")
        sys.exit(127)
    
    # Then check if the file is an Excel file
    if not input_excel_path.lower().endswith(('.xlsx', '.xls')):
        print(Fore.RED, "Invalid Excel file. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid Excel file: {input_excel_path}")
        sys.exit(127)

    # Open the Excel file
    workbook = openpyxl.load_workbook(filename=input_excel_path)
    # Get the active worksheet
    worksheet = workbook.active

    headers = []
    header_row = worksheet[1]
    # Delete the header row
    worksheet.delete_rows(0)
    # Loop through the header row and add each cell's value to the headers list
    for header_cell in header_row:
        headers.append(header_cell.value)

    records = []
    # Loop through the rows in the worksheet and add each row's data to the records list
    for row in worksheet.iter_rows(min_row=1):
        record = {}
        for index, cell in enumerate(row):
            if headers[index] is not None and cell.value is not None:
                record[headers[index]] = cell.value
        records.append(record)

    csv_data = StringIO()
    csv_writer = csv.DictWriter(csv_data, fieldnames=headers)
    csv_writer.writeheader()
    for record in records:
        csv_writer.writerow(record)

    csv_data.seek(0)
    return csv.DictReader(csv_data)

def extract_csv(input_csv_path) -> csv.DictReader:
    """Open the CSV file at <input_csv_path> and return a DictReader object containing the CSV data."""
    if not os.path.exists(input_csv_path):
        print(Fore.RED, "Invalid CSV file path. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid CSV file path: {input_csv_path}")
        sys.exit(127)

    if not input_csv_path.lower().endswith('.csv'):
        print(Fore.RED, "Invalid CSV file. Please see the log for more details.", Fore.RESET)
        logging.error(f"Invalid CSV file: {input_csv_path}")
        sys.exit(127)

    with open(input_csv_path, "r", newline='') as csv_file:
        csv_data = csv_file.read()

    csv_data_stream = io.StringIO(csv_data)
    return csv.DictReader(csv_data_stream)

def dictreader_to_dictionaries(csv_data: csv.DictReader) -> list:
    """ Convert the CSV data in <csv_data> to a list of dictionaries and return a DictReader object containing the data."""
    formatted_data = []
    for row in csv_data:
        formatted_row = {}
        for key, value in row.items():
            key = key.lower() if isinstance(key, str) else key
            key = key.replace(" ", "_") if isinstance(key, str) else key
            value = value.lower().replace(" ", "_") if isinstance(value, str) and key == "test_type" else value
            formatted_row[key] = value
        formatted_data.append(formatted_row)

    return formatted_data

def check_data(data: list) -> None:
    """ Validate the data and exit the program if any errors are found."""
    # Check if there is no data
    if len(data) == 0:
        print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
        logging.error("Invalid CSV file. The CSV file is empty.")
        sys.exit(127)

    supported_test_types = ["site_availability_test", 
                            "facet_load_test", 
                            "collection_count_test", 
                            "openseadragon_load_test", 
                            "mirador_viewer_load_test", 
                            "mirador_page_count_test",
                            "ableplayer_load_test",
                            "ableplayer_transcript_load_test"]
    row_number = 1
    for row in track(data, description="Verifying CSV File..."):
        # Check if the CSV file contains the required fields
        if "url" not in row:
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. URL column is missing from row {row_number + 1}")
            sys.exit(127)
        if row["url"] == "":
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. URL column is empty in row {row_number + 1}")
            sys.exit(127)
        if "test_type" not in row:
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Type column is missing from row {row_number + 1}")
            sys.exit(127)
        if row["test_type"] not in supported_test_types:
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Type column contains an invalid test type ({row['test_type']}) in row {row_number + 1}")
            sys.exit(127)
        
        # Check specific fields for specific test types
        # Facet Load Tests need a string input representing the facet name
        if row["test_type"] == "facet_load_test" and "test_input" not in row:
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Input column is missing from row {row_number + 1}")
            sys.exit(127)
        if row["test_type"] == "facet_load_test" and row["test_input"] == "":
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Input column is empty in row {row_number + 1}")
            sys.exit(127)
        
        # Collection Count Tests need an integer input representing the expected number of collections
        if row["test_type"] == "collection_count_test" and "test_input" not in row:
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Input column is missing from row {row_number + 1}")
            sys.exit(127)
        if row["test_type"] == "collection_count_test" and row["test_input"] == "":
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Input column is empty in row {row_number + 1}")
            sys.exit(127)

        # Mirador Viewer Page Count Tests need an integer input representing the expected number of thumbnails
        if row["test_type"] == "mirador_page_count_test" and "test_input" not in row:
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Input column is missing from row {row_number + 1}")
            sys.exit(127)
        if row["test_type"] == "mirador_viewer_load_test" and row["test_input"] == "":
            print(Fore.RED, "Invalid CSV file. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid CSV file. Test Input column is empty in row {row_number + 1}")
            sys.exit(127)
        
        row_number += 1
    
    # If the CSV file is valid, print a success message
    print(Fore.GREEN, "CSV file is valid.")
    logging.info("CSV file is valid.")

def extract_data(config: dict) -> list:
    """ Extract the test data from either a Google Sheet, Excel file, or CSV file (specified in <config>) and return a formatted DictReader object 
    containing the data."""
    if 'google_sheets' in config:
        data = dictreader_to_dictionaries(extract_google_sheet(config['google_sheets']))
        check_data(data)
        return data
    elif 'excel' in config:
        data = dictreader_to_dictionaries(extract_excel(config['excel']))
        check_data(data)
        return data
    elif 'csv' in config:
        data = dictreader_to_dictionaries(extract_csv(config['csv']))
        check_data(data)
        return data
    else:
        print(Fore.RED, "Invalid data source. Please see the log for more details.", Fore.RESET)
        logging.error(f"There is no valid data source specified in the config file. Please specify either a Google Sheets URL, Excel file path, \
                      or CSV file path.")
        sys.exit(127)