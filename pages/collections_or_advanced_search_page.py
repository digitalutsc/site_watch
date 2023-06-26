"""
This module contains the CollectionsOrAdvancedSearchPage class, which represents a page displaying a collections or an
advanced search page.

The CollectionsOrAdvancedSearchPage class inherits from the BasePage class and provides methods for getting the number
of collections on the collections page.
"""

from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.page import BasePage


class CollectionsOrAdvancedSearchPage(BasePage):
    """
    A class representing a page displaying collections or an advanced search page.

    This class inherits from the BasePage class and provides methods for getting the number of collections on the collections
    page.
    """
    driver: WebDriver  # The driver used to load the page
    url: str  # The URL of the page

    def get_collection_count(self) -> Optional[int]:
        """Return the number of collections on the collections page."""
        self.driver.get(self.url)
        try:
            # Get the element displaying "x - y of z"
            pager_summary = self.driver.find_element(By.CLASS_NAME, "pager__summary")
            return int(pager_summary.text.split(" ")[-1])  # We only need the last number (z)
        except NoSuchElementException:
            return None