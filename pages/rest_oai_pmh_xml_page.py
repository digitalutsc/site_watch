"""
This module contains the RestOAIPMHXMLPage class, which represents a page displaying OAI-PMH XML data.

The RestOAIPMHXMLPage class inherits from the BasePage class and provides a method for checking whether the XML on the
page is valid.
"""

import requests

from selenium.webdriver.remote.webdriver import WebDriver
from pages.page import BasePage


class RestOAIPMHXMLPage(BasePage):
    """
    A class representing a page displaying OAI-PMH XML data.

    The RestOAIPMHXMLPage class inherits from the BasePage class and provides a method for checking whether the XML on the
    page is valid.
    """
    driver: WebDriver  # The driver used to load the page
    url: str  # The URL of the page
    def is_valid_xml(self) -> bool:
        """Return whether the XML on the page is valid."""
        # There are two things that would make it invalid.
        #   - The page is unavailable as per `is_available()`
        #   - The XML on the page contains "idDoesNotExist" or "badVerb"
        if self.is_available():
            # Send a request to get the text
            response_text = requests.get(self.url).text
            if "idDoesNotExist" in response_text or "badVerb" in response_text:
                return False
            return True
        return False
