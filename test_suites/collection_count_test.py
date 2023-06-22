"""
This module contains the CollectionCountTest class, which is a test to check that the number of collections on the collections
page is correct.

The CollectionCountTest class inherits from the Test class and provides a method for running the test on a given URL and
comparing the result to an expected value.
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from pages.collections_or_advanced_search_page import CollectionsOrAdvancedSearchPage
from test_suites.test import Test


class CollectionCountTest(Test):
    """
    A test to check that the number of collections on the collections page is correct.

    The CollectionCountTest class inherits from the Test class and provides a method for running the test on a given URL
    and comparing the result to an expected value.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str, expected_value: str) -> None:
        """ Run the collection count test on the page at <url> with <expected_value>."""
        try:
            expected_value = int(expected_value)
        except ValueError:
            raise ValueError(f"Expected value must be an integer, but got {expected_value}.")
        collection_page = CollectionsOrAdvancedSearchPage(self.driver, url)
        try:
            actual_value = int(collection_page.get_collection_count())
        except NoSuchElementException:
            raise NoSuchElementException(f"Could not find the collections count at {url}.")
        assert actual_value == expected_value, f"Expected {expected_value}, but got {actual_value}."
