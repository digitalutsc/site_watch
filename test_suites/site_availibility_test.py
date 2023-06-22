"""
This module contains the SiteAvailabilityTest class, which is a test to check whether a given web page is available.

The SiteAvailabilityTest class inherits from the Test class and provides a method for running the test on a given URL.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from pages.page import BasePage
from test_suites.test import Test


class SiteAvailabilityTest(Test):
    """
    A test to check whether a given web page is available.

    The SiteAvailabilityTest class inherits from the Test class and provides a method for running the test on a given URL.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str):
        """ Run the site availability test on the page at <url>."""
        base_page = BasePage(self.driver, url)
        assert base_page.is_available(), f"Page at {url} is not available."
