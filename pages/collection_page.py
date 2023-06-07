from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.page import BasePage

class CollectionPage(BasePage):
    """A page representing a collection."""
    def is_openseadragon_loads(self) -> bool:
        """Return whether the openseadragon viewer loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "openseadragon-container").find_element(By.TAG_NAME, "canvas")
            return True
        except NoSuchElementException:
            return False
    
    def is_mirador_loads(self) -> bool:
        """Return whether the mirador viewer loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "mirador-viewer").find_element(By.TAG_NAME, "canvas")
            return True
        except NoSuchElementException:
            return False
    
    def is_ableplayer_loads(self) -> bool:
        """Return whether the ableplayer loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "able").find_element(By.TAG_NAME, "video")
            return True
        except NoSuchElementException:
            return False
    
    def is_ableplayer_transcript_loads(self) -> bool:
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "able-transcript")
            return True
        except NoSuchElementException:
            return False