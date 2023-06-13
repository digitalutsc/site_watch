from selenium import webdriver
from colorama import Fore
import logging
from test_suites.collection_count_test import CollectionCountTest
from test_suites.facet_load_test import FacetLoadTest
from test_suites.site_availibility_test import SiteAvailabilityTest
from test_suites.viewer_tests import OpenSeaDragonLoadTest, MiradorLoadTest, MiradorPageCountTest, AblePlayerLoadTest, AblePlayerTranscriptLoadTest

logging = logging.getLogger(__name__)

class TestController():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.collection_count_test = CollectionCountTest(self.driver)
        self.facet_load_test = FacetLoadTest(self.driver)
        self.site_availability_test = SiteAvailabilityTest(self.driver)
        self.openseadragon_load_test = OpenSeaDragonLoadTest(self.driver)
        self.mirador_load_test = MiradorLoadTest(self.driver)
        self.mirador_page_count_test = MiradorPageCountTest(self.driver)
        self.ableplayer_load_test = AblePlayerLoadTest(self.driver)
        self.ableplayer_transcript_load_test = AblePlayerTranscriptLoadTest(self.driver)
        self.driver.implicitly_wait(10)
    
    def run_collection_count_test(self, csv_row: dict, csv_row_number: int) -> bool:
        """ Runs a Collection Count Test. """
        try:
            self.collection_count_test.run(csv_row["url"], csv_row["test_input"])
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
        
    def run_facet_load_test(self, csv_row: dict, csv_row_number: int) -> bool:
        """ Runs a Facet Load Test. """
        try:
            self.facet_load_test.run(csv_row["url"], csv_row["test_input"])
        except ValueError:
            # The facet type is invalid.
            print(Fore.RED, f"Invalid test input on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Invalid facet type {csv_row['test_input']} on row {csv_row_number + 1}. The test input must be a valid facet type.")
            return False
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Facet Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Facet Load Test failed on row {csv_row_number + 1}. The facet did not load. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Facet Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Facet Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Facet Load Test passed on row {csv_row_number + 1}.")
            logging.info(f"Facet Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_site_availibility_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Site Availibility Test. """
        try:
            self.site_availability_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Site Availability Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Site Availability Test failed on row {csv_row_number + 1}. The site was not available. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Site Availability Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Site Availability Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Site Availability Test passed on row {csv_row_number + 1}.")
            logging.info(f"Site Availability Test passed on row {csv_row_number + 1}.")
            return True

    def run_openseadragon_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an OpenSeaDragon Load Test. """
        try:
            self.openseadragon_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. The viewer did not load. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"OpenSeaDragon Load Test passed on row {csv_row_number + 1}.")
            logging.info(f"OpenSeaDragon Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_mirador_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Mirador Load Test. """
        try:
            self.mirador_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Mirador Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Mirador Load Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Mirador Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Mirador Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Mirador Load Test passed on row {csv_row_number + 1}.")
            logging.info(f"Mirador Load Test passed on row {csv_row_number + 1}.")
            return True
    
    def run_mirador_page_count_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Mirador Page Count Test. """
        try:
            self.mirador_page_count_test.run(csv_row["url"], int(csv_row["test_input"]))
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Mirador Page Count Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Mirador Page Count Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Mirador Page Count Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Mirador Page Count Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Mirador Page Count Test passed on row {csv_row_number + 1}.")
            logging.info(f"Mirador Page Count Test passed on row {csv_row_number + 1}.")
            return True

    def run_ableplayer_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an AblePlayer Load Test. """
        try:
            self.ableplayer_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"AblePlayer Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"AblePlayer Load Test failed on row {csv_row_number + 1}. The viewer did not load. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"AblePlayer Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"AblePlayer Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"AblePlayer Load Test passed on row {csv_row_number + 1}.")
            logging.info(f"AblePlayer Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_ableplayer_transcript_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an AblePlayer Transcript Load Test. """
        try:
            self.ableplayer_transcript_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"AblePlayer Transcript Load Test passed on row {csv_row_number + 1}.")
            logging.info(f"AblePlayer Transcript Load Test passed on row {csv_row_number + 1}.")
            return True
    
    def run_test(self, csv_row: dict, csv_row_number: int) -> bool:
        """ Runs a test based on the test type specified in <csv_row>. """
        test_type = csv_row["test_type"]
        if test_type == 'collection_count_test':
            test_result = self.run_collection_count_test(csv_row, csv_row_number)
        elif test_type == 'facet_load_test':
            test_result = self.run_facet_load_test(csv_row, csv_row_number)
        elif test_type == 'site_availability_test':
            test_result = self.run_site_availibility_test(csv_row, csv_row_number)
        elif test_type == 'openseadragon_load_test':
            test_result = self.run_openseadragon_load_test(csv_row, csv_row_number)
        elif test_type == 'mirador_viewer_load_test':
            test_result = self.run_mirador_load_test(csv_row, csv_row_number)
        elif test_type == 'mirador_page_count_test':
            test_result = self.run_mirador_page_count_test(csv_row, csv_row_number)
        elif test_type == 'ableplayer_load_test':
            test_result = self.run_ableplayer_load_test(csv_row, csv_row_number)
        elif test_type == 'ableplayer_transcript_load_test':
            test_result = self.run_ableplayer_transcript_load_test(csv_row, csv_row_number)
        else:
            print(Fore.RED, f"Test type on row {csv_row_number + 1} is not supported. Please see log for more details.")
            logging.error(f"Test type {test_type} on row {csv_row_number + 1} is not supported.")
            test_result = False
        return test_result
    
    def tear_down(self):
        """ Tears down the test. """
        self.driver.quit()
