from pages.collections_or_advanced_search_page import CollectionsOrAdvancedSearchPage
from tests.test import Test
from selenium.common.exceptions import NoSuchElementException

class CollectionCountTest(Test):
    """ A test to check that the number of collections on the collections page is correct. """    
    def run(self, url: str, expected_value: str) -> None:
        """ Run the test on the page at <url> and compare the result to <expected_value>."""
        try:
            expected_value = int(expected_value)
        except ValueError:
            raise ValueError(f"Expected value must be an integer, but got {expected_value}.")
        collection_page = CollectionsOrAdvancedSearchPage(self.driver, url)
        try:
            actual_value = int(collection_page.get_collection_count())
        except NoSuchElementException:
            raise NoSuchElementException(f"Could not find the collections count on {url}.")
        assert actual_value == expected_value, f"Expected {expected_value}, but got {actual_value}."
