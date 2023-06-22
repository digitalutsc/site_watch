"""
This module contains the InvalidLinksTest class, which is a test to check whether a given web page has any invalid links.

The InvalidLinksTest class inherits from the Test class and provides a method for running the test on a given URL.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from test_suites.test import Test
from pages.page import BasePage


class InvalidLinksTest(Test):
    """
    A test to check whether a given web page has any invalid links.

    The InvalidLinksTest class inherits from the Test class and provides a method for running the test on a given URL.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str) -> None:
        """ Run the invalid links test on the page at <url>."""
        invalid_links = BasePage(self.driver, url).invalid_links()
        assert len(invalid_links) == 0, f"Page with URL {url} has invalid links. Particular links: {invalid_links}"
