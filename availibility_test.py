from page import BasePage
from test import Test

class AvailabilityTest(Test):
    def run(self, url: str):
        base_page = BasePage(self.driver, url)
        assert base_page.is_available(), f"Page at {url} is not available."