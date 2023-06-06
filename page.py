from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests

class BasePage(object):
    def __init__(self, driver: WebDriver, url: str) -> None:
        self.driver = driver
        self.url = url
    
    def is_available(self) -> bool:
        """Return whether the page is available."""
        return requests.get(self.url).status_code in [200, 201]
        
    
class CollectionPage(BasePage):
    def get_collection_count(self) -> int:
        """Return the number of collections on the collections page."""
        self.driver.get(self.url)
        pager_summary = self.driver.find_element(By.CSS_SELECTOR, "#block-barriodepartments-collectionsearchresultspagerforpage > div > div.pager__summary")
        return int(pager_summary.text.split(" ")[-1])
    
    def is_subject_facet_present(self) -> bool:
        """Return whether the subject facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-barriodepartments-subject")
            return True
        except:
            return False
    
    def is_genre_facet_present(self) -> bool:
        """Return whether the genre facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-barriodepartments-genre")
            return True
        except:
            return False
    
    def is_publication_date_facet_present(self) -> bool:
        """Return whether the publication date facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-barriodepartments-publicationdatecollection")
            return True
        except:
            return False
    
    def is_related_archival_fonds_facet_present(self) -> bool:
        """Return whether the related archival fonds facet is present on the collections page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.ID, "block-relatedarchivalfondstesting")
            return True
        except:
            return False