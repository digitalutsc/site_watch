"""
This module contains the FacetLoadTest class, which is a test to check whether a given facet is present on a collections page.

The FacetLoadTest class inherits from the Test class and provides a method for running the test on a given URL and facet type.
"""

from selenium.webdriver.remote.webdriver import WebDriver

from test_suites.test import Test
from pages.collections_or_advanced_search_page import CollectionsOrAdvancedSearchPage


class FacetLoadTest(Test):
    """
    A test to check whether a given facet is present on a collections page.

    The FacetLoadTest class inherits from the Test class and provides a method for running the test on a given URL and facet type.
    """
    driver: WebDriver  # The driver used to load the page

    def run(self, url: str, facet_type: str) -> None:
        """ Run the facet load test with <facet_type> on the page at <url>."""
        collection_page = CollectionsOrAdvancedSearchPage(self.driver, url)
        if facet_type == "subject":
            assert collection_page.is_subject_facet_present(), "Subject facet is not present on collections page."
        elif facet_type == "genre":
            assert collection_page.is_genre_facet_present(), "Genre facet is not present on collections page."
        elif facet_type == "publication_date":
            assert collection_page.is_publication_date_facet_present(), "Publication date facet is not present on collections page."
        elif facet_type == "related_archival_fonds":
            assert collection_page.is_related_archival_fonds_facet_present(), "Related archival fonds facet is not present on collections page."
        else:
            raise ValueError(f"Invalid facet type: {facet_type}.")
