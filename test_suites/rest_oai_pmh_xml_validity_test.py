"""
This module contains the RestOAIPMHXMLValidityTest class, which is a test to check that the rest_oai_pmh_xml page is valid XML.

The RestOAIPMHXMLValidityTest class inherits from the Test class and provides a method for running the test on a given URL.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from pages.rest_oai_pmh_xml_page import RestOAIPMHXMLPage
from test_suites.test import Test


class RestOAIPMHXMLValidityTest(Test):
    """
    A test to check that the rest_oai_pmh_xml page is valid XML.

    The RestOAIPMHXMLValidityTest class inherits from the Test class and provides a method for running the test on a given URL.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str) -> None:
        """ Run the rest_oai_pmh_xml validity test on the page at <url>."""
        rest_oai_pmh_xml_page = RestOAIPMHXMLPage(self.driver, url)
        assert rest_oai_pmh_xml_page.is_valid_xml(), "REST OAI PMH XML page is not valid XML."
