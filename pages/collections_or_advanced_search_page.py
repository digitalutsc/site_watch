"""
This module contains the CollectionsOrAdvancedSearchPage class, which represents a page displaying a collections or an
advanced search page.

The CollectionsOrAdvancedSearchPage class inherits from the BasePage class and provides methods for getting the number
of collections on the collections page and checking whether various facets (subject, genre, publication date, related
archival fonds) are present on the page.
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
    page and checking whether various facets (subject, genre, publication date, related archival fonds) are present on the page.
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

    def is_subject_facet_present(self) -> bool:
        """Return whether the subject facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-barriodepartments-subject")
            return True
        except NoSuchElementException:
            return False

    def is_genre_facet_present(self) -> bool:
        """Return whether the genre facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-barriodepartments-genre")
            return True
        except NoSuchElementException:
            return False

    def is_publication_date_facet_present(self) -> bool:
        """Return whether the publication date facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-barriodepartments-publicationdatecollection")
            return True
        except NoSuchElementException:
            return False

    def is_related_archival_fonds_facet_present(self) -> bool:
        """Return whether the related archival fonds facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-relatedarchivalfondstesting")
            return True
        except NoSuchElementException:
            return False
