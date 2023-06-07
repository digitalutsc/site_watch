from pages.page import BasePage
from tests.test import Test

class SiteAvailabilityTest(Test):
    def run(self, url: str):
        base_page = BasePage(self.driver, url)
        assert base_page.is_available(), f"Page at {url} is not available."