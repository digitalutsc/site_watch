from pages.page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from typing import Optional


class CollectionsOrAdvancedSearchPage(BasePage):
    def get_collection_count(self) -> Optional[int]:
        """Return the number of collections on the collections page."""
        self.driver.get(self.url)
        try:
            pager_summary = self.driver.find_element(By.CLASS_NAME, "pager__summary")
            return int(pager_summary.text.split(" ")[-1])
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
