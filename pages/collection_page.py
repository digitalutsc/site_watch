from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
    
    def get_mirador_page_count(self) -> int:
        """Return the number of pages in the mirador viewer, None if not present."""
        self.driver.get(self.url)
        try:
            # count = 0
            # start_time = time.time()
            # while count == 0 and time.time() - start_time < 40:  # Loop until either the count is found or 40 seconds have passed
            #     count = int(self.driver.find_elements(By.XPATH, "//*[contains(text(), '1 of ')]")[0].text.split(" ")[2])
            # return count
            self.driver.implicitly_wait(40)
            count = self.driver.find_elements(By.XPATH, "//*[contains(text(), '1 of ') and not(contains(text(), '1 of 0'))]")[0].text.split(" ")[2]
            return int(count)
        except NoSuchElementException:
            return None

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