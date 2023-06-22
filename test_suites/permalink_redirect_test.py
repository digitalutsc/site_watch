"""
This module contains the PermalinkRedirectTest class, which is a test to check whether a given permalink redirects to the expected URL.

The PermalinkRedirectTest class inherits from the Test class and provides a method for running the test on a given URL and expected URL.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from pages.collection_page import CollectionPage
from test_suites.test import Test


class PermalinkRedirectTest(Test):
    """
    A test to check whether a given permalink redirects to the expected URL.

    The PermalinkRedirectTest class inherits from the Test class and provides a method for running the test on a given URL and expected URL.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str, expected_url: str) -> None:
        """ Run the permalink redirect test on the page at <url>."""
        collection_page = CollectionPage(self.driver, url)
        actual_url = collection_page.get_permalink_redirect_url()
        assert actual_url == expected_url, f"Expected {expected_url}, but got {actual_url}."
