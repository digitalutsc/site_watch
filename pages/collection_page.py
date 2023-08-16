"""
This module contains the CollectionPage class, which represents a page displaying a collection item.

The CollectionPage class inherits from the BasePage class and provides methods for checking whether various viewers
(OpenSeadragon, Mirador, Ableplayer) load on the page, getting the number of pages in the mirador viewer, and getting
the URL that the ARK permalink redirects to.
"""

from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.page import BasePage


class CollectionPage(BasePage):
    """
    A class representing a page displaying a collection.

    This class inherits from the BasePage class and provides methods for checking whether various viewers
    (openseadragon, mirador, ableplayer) load on the page, getting the number of pages in the mirador viewer, and getting
    the URL that the permalink redirects to.
    """
    driver: WebDriver  # The driver used to load the page
    url: str  # The URL of the page

    def is_openseadragon_loads(self) -> bool:
        """Return whether the OpenSeadragon viewer loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "openseadragon-container").find_element(By.TAG_NAME, "canvas")
            return True
        except NoSuchElementException:
            return False

    def is_mirador_loads(self) -> bool:
        """Return whether the Mirador viewer loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.implicitly_wait(40)  # Wait up to 40 seconds for the element to appear
            self.driver.find_element(By.CLASS_NAME, "mirador-viewer").find_element(By.TAG_NAME, "canvas")
            self.driver.implicitly_wait(20)  # Reset the implicit wait
            return True
        except NoSuchElementException:
            self.driver.implicitly_wait(20)  # Reset the implicit wait
            return False

    def get_mirador_page_count(self) -> Optional[int]:
        """Return the number of pages in the Mirador viewer, None if the viewer is not present."""
        self.driver.get(self.url)
        try:
            self.driver.implicitly_wait(40)  # Wait up to 40 seconds for the element to appear
            count = self.driver.find_elements(By.XPATH, "//*[contains(text(), '1 of ') and not(contains(text(), '1 of 0'))]")[0].text.split(" ")[2]
            self.driver.implicitly_wait(20)  # Reset the implicit wait
            return int(count)
        except NoSuchElementException:
            self.driver.implicitly_wait(20)  # Reset the implicit wait
            return None

    def is_ableplayer_loads(self) -> bool:
        """Return whether the ableplayer loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "able")
            return True
        except NoSuchElementException:
            return False

    def is_ableplayer_transcript_loads(self) -> bool:
        """Return whether the ableplayer transcript loads on the page."""
        self.driver.get(self.url)
        try:
            self.driver.find_element(By.CLASS_NAME, "able-transcript")
            return True
        except NoSuchElementException:
            return False

    def get_permalink_redirect_url(self) -> Optional[str]:
        """Return the url that the permalink redirects to, None if not present."""
        self.driver.get(self.url)
        try:
            permalink_url = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/main/section/section/div[5]/div/div/div/div/div/div/span/div/div[3]/a"
            ).get_attribute("href")
            self.driver.get(permalink_url)
            return self.driver.current_url
        except NoSuchElementException:
            return None
