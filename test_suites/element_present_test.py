from test_suites.test import Test
from pages.page import BasePage

class ElementPresentTest(Test):
    def run(self, url: str, method: str, selector: str) -> None:
        page = BasePage(self.driver, url)
        assert page.is_contains_element(method, selector), f"Element with selector {selector} is not present on page with URL {url}."
