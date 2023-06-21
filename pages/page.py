from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

class BasePage(object):
    def __init__(self, driver: WebDriver, url: str) -> None:
        """Initialize the page with a driver and a URL. It is assumed that the URL is valid."""
        self.driver = driver
        self.url = url
    
    def is_available(self) -> bool:
        """Return whether the page is available."""
        response = requests.get(self.url)
        if response.status_code in [200, 201] and "Page not found" not in response.text.lower():
            try:
                self.driver.get(self.url)
                return True
            except:
                return False
        return False
    
    def is_contains_element(self, method: str, selector: str) -> bool:
        """Return whether the page contains an element with the given selector."""
        self.driver.get(self.url)
        try:
            if method == "id":
                self.driver.find_element(By.ID, selector)
            elif method == "class":
                self.driver.find_element(By.CLASS_NAME, selector)
            elif method == "css":
                self.driver.find_element(By.CSS_SELECTOR, selector)
            elif method == "xpath":
                self.driver.find_element(By.XPATH, selector)
            else:
                raise ValueError("Invalid method.")
            return True
        except NoSuchElementException:
            return False
    
    def invalid_links(self) -> list:
        """Return a list of invalid links on the page.
        
        This method is multi-threaded.
        """

        def check_link(link) -> Optional[str]:
            """Check if a link is valid. Return the link if it is invalid, otherwise return None."""
            page = BasePage(self.driver, link)
            if not page.is_available():
                return link
            return None

        self.driver.get(self.url)
        invalid_links = []  # Will contain the list of invalid links
        links = [link.get_attribute("href") for link in self.driver.find_elements(By.TAG_NAME, "a")]  # Get all links on the page
        # Check each link. The below code is multi-threaded.
        with ThreadPoolExecutor() as executor:
            results = executor.map(check_link, links)
        # Filter the invalid links and return them
        invalid_links = [link for link in results if link is not None]
        return invalid_links
