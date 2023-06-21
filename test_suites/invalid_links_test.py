from test_suites.test import Test
from pages.page import BasePage

class InvalidLinksTest(Test):
    def run(self, url: str) -> None:
        invalid_links = BasePage(self.driver, url).invalid_links()
        assert len(invalid_links) == 0, f"Page with URL {url} has invalid links. Particular links: {invalid_links}"
