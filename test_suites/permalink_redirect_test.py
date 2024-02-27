"""
This module contains the PermalinkRedirectTest class, which is a test to check whether a given permalink redirects to the expected URL.

The PermalinkRedirectTest class inherits from the Test class and provides a method for running the test on a given URL and expected URL.
"""

from selenium.webdriver.remote.webdriver import WebDriver

# from pages.collection_page import CollectionPage
from pages.page import BasePage
from test_suites.test import Test


class PermalinkRedirectTest(Test):
    """
    A test to check whether a given permalink redirects to the expected URL.

    The PermalinkRedirectTest class inherits from the Test class and provides a method for running the test on a given URL and expected URL.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str, expected_url: str) -> None:
        """ Run the permalink redirect test on the page at <url>."""
        self.driver.get(url) # load page
        redirect_url = self.driver.current_url # get the [new] url of the page that is loaded by webdriver

        redirect_page = BasePage(self.driver, redirect_url) 
        if redirect_page.is_available(): # check if the page loaded has 2xx response code (i.e. has properly loaded)
            expected_url_revised = expected_url.rstrip("/") 
            redirect_url_revised = redirect_url.rstrip("/") 
            # NOTE: test fails if you remove the trailing / of the expected url
            assert redirect_url_revised == expected_url_revised, f"Expected {expected_url_revised}, but got {redirect_url_revised}." 
        else:
            assert redirect_page.is_available(), f"Permalink did not redirect with 2xx response code."