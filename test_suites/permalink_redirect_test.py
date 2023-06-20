from pages.collection_page import CollectionPage
from test_suites.test import Test

class PermalinkRedirectTest(Test):
    def run(self, url: str, expected_url: str) -> None:
        """ Run the test on the page at <url> and compare the result to <expected_value>."""
        collection_page = CollectionPage(self.driver, url)
        actual_url = collection_page.get_permalink_redirect_url()
        assert actual_url == expected_url, f"Expected {expected_url}, but got {actual_url}."
