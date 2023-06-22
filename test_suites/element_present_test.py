"""
This module contains the ElementPresentTest class, which is a test to check whether a given element is present on a web page.

The ElementPresentTest class inherits from the Test class and provides a method for running the test on a given URL and
selector.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from test_suites.test import Test
from pages.page import BasePage


class ElementPresentTest(Test):
    """
    A test to check whether a given element is present on a web page.

    The ElementPresentTest class inherits from the Test class and provides a method for running the test on a given URL and
    selector.
    """
    driver: WebDriver  # The driver used to load the page
    
    def run(self, url: str, method: str, selector: str) -> None:
        """ Run the element present test with <method> and <selector> on the page at <url>."""
        page = BasePage(self.driver, url)
        assert page.is_contains_element(method, selector), f"Element with selector {selector} is not present on page with URL {url}."
