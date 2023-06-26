"""
This module contains the TestController class, which is a master controller for every type of test.

The main method of this class is the run_test method.
"""

import logging

from colorama import Fore
from selenium import webdriver

from test_suites.collection_count_test import *
from test_suites.element_present_test import *
from test_suites.invalid_links_test import *
from test_suites.permalink_redirect_test import *
from test_suites.rest_oai_pmh_xml_validity_test import *
from test_suites.site_availibility_test import *
from test_suites.viewer_tests import *

logging = logging.getLogger(__name__)


class TestController():
    """
    A master controller for every type of test.
    """
    def __init__(self):
        # Initialize the driver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(20)

        # Warm up the driver
        self.driver.get("https://google.com")

        # Initialize the tests
        self.collection_count_test = CollectionCountTest(self.driver)
        self.site_availability_test = SiteAvailabilityTest(self.driver)
        self.openseadragon_load_test = OpenSeaDragonLoadTest(self.driver)
        self.mirador_load_test = MiradorLoadTest(self.driver)
        self.mirador_page_count_test = MiradorPageCountTest(self.driver)
        self.ableplayer_load_test = AblePlayerLoadTest(self.driver)
        self.ableplayer_transcript_load_test = AblePlayerTranscriptLoadTest(self.driver)
        self.element_present_test = ElementPresentTest(self.driver)
        self.invalid_links_test = InvalidLinksTest(self.driver)
        self.permalink_redirect_test = PermalinkRedirectTest(self.driver)
        self.rest_oai_pmh_xml_validity_test = RestOAIPMHXMLValidityTest(self.driver)

    def run_collection_count_test(self, csv_row: dict, csv_row_number: int) -> bool:
        """ Runs a Collection Count Test. """
        try:
            self.collection_count_test.run(csv_row["url"], csv_row["test_input"])
        except ValueError:
            print(Fore.RED, f"Invalid test input on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid test input on row {csv_row_number + 1}. The test input must be an integer.")
            return False
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Collection Count Test failed on row {csv_row_number + 1}. Please see log for more details.")
            logging.error(f"Collection Count Test failed on row {csv_row_number + 1}. The expected number of collections was not found. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Collection Count Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Collection Count Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Collection Count Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Collection Count Test passed on row {csv_row_number + 1}.")
            return True

    def run_site_availibility_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Site Availibility Test. """
        try:
            self.site_availability_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Site Availability Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Site Availability Test failed on row {csv_row_number + 1}. The site was not available. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Site Availability Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Site Availability Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Site Availability Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Site Availability Test passed on row {csv_row_number + 1}.")
            return True

    def run_openseadragon_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an OpenSeaDragon Load Test. """
        try:
            self.openseadragon_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. The viewer did not load. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"OpenSeaDragon Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"OpenSeaDragon Load Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"OpenSeaDragon Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_mirador_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Mirador Load Test. """
        try:
            self.mirador_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Mirador Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Mirador Load Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Mirador Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Mirador Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Mirador Load Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Mirador Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_mirador_page_count_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Mirador Page Count Test. """
        try:
            self.mirador_page_count_test.run(csv_row["url"], int(csv_row["test_input"]))
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Mirador Page Count Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Mirador Page Count Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Mirador Page Count Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Mirador Page Count Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Mirador Page Count Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Mirador Page Count Test passed on row {csv_row_number + 1}.")
            return True

    def run_ableplayer_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an AblePlayer Load Test. """
        try:
            self.ableplayer_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"AblePlayer Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"AblePlayer Load Test failed on row {csv_row_number + 1}. The viewer did not load. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"AblePlayer Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"AblePlayer Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"AblePlayer Load Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"AblePlayer Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_ableplayer_transcript_load_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an AblePlayer Transcript Load Test. """
        try:
            self.ableplayer_transcript_load_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"AblePlayer Transcript Load Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"AblePlayer Transcript Load Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"AblePlayer Transcript Load Test passed on row {csv_row_number + 1}.")
            return True

    def run_element_present_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an Element Present Test. """
        try:
            self.element_present_test.run(csv_row["url"], *(csv_row["test_input"].split('|')))
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Element Present Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Element Present Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except ValueError as e:
            # Get the ValueError message
            error_message = str(e)
            print(Fore.RED, f"Element Present Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Element Present Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Element Present Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Element Present Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Element Present Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Element Present Test passed on row {csv_row_number + 1}.")
            return True

    def run_invalid_links_test(self, csv_row: dict, csv_row_number: int):
        """ Runs an Invalid Links Test. """
        try:
            self.invalid_links_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Invalid Links Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid Links Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Invalid Links Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Invalid Links Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Invalid Links Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Invalid Links Test passed on row {csv_row_number + 1}.")
            return True

    def run_permalink_redirect_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a Permalink Redirect Test. """
        try:
            self.permalink_redirect_test.run(csv_row["url"], csv_row["test_input"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"Permalink Redirect Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Permalink Redirect Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"Permalink Redirect Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"Permalink Redirect Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"Permalink Redirect Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"Permalink Redirect Test passed on row {csv_row_number + 1}.")
            return True

    def run_rest_oai_pmh_xml_validity_test(self, csv_row: dict, csv_row_number: int):
        """ Runs a REST OAI-PMH XML Validity Test. """
        try:
            self.rest_oai_pmh_xml_validity_test.run(csv_row["url"])
        except AssertionError as e:
            # Get the assertion error message
            error_message = str(e)
            print(Fore.RED, f"REST OAI-PMH XML Validity Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"REST OAI-PMH XML Validity Test failed on row {csv_row_number + 1}. {error_message}")
            return False
        except Exception as e:
            print(Fore.RED, f"REST OAI-PMH XML Validity Test failed on row {csv_row_number + 1}. Please see log for more details.", Fore.RESET)
            logging.error(f"REST OAI-PMH XML Validity Test failed on row {csv_row_number + 1}. {e}")
            return False
        else:
            print(Fore.GREEN, f"REST OAI-PMH XML Validity Test passed on row {csv_row_number + 1}.", Fore.RESET)
            logging.info(f"REST OAI-PMH XML Validity Test passed on row {csv_row_number + 1}.")
            return True

    def run_test(self, csv_row: dict, csv_row_number: int) -> bool:
        """ Runs a test based on the test type specified in <csv_row>. """
        test_type = csv_row["test_type"]
        test_methods = {
            'collection_count_test': self.run_collection_count_test,
            'site_availability_test': self.run_site_availibility_test,
            'openseadragon_load_test': self.run_openseadragon_load_test,
            'mirador_viewer_load_test': self.run_mirador_load_test,
            'mirador_page_count_test': self.run_mirador_page_count_test,
            'ableplayer_load_test': self.run_ableplayer_load_test,
            'ableplayer_transcript_load_test': self.run_ableplayer_transcript_load_test,
            'element_present_test': self.run_element_present_test,
            'invalid_links_test': self.run_invalid_links_test,
            'permalink_redirect_test': self.run_permalink_redirect_test,
            'rest_oai_pmh_xml_validity_test': self.run_rest_oai_pmh_xml_validity_test
        }
        test_method = test_methods.get(test_type)
        if test_method is None:
            print(Fore.RED, f"Test type on row {csv_row_number + 1} is not supported. Please see log for more details.", Fore.RESET)
            logging.error(f"Test type {test_type} on row {csv_row_number + 1} is not supported.")
            return False
        return test_method(csv_row, csv_row_number)

    def tear_down(self):
        """ Tears down the test. """
        self.driver.quit()
