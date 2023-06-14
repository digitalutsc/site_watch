from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
from typing import Optional

class BasePage(object):
    def __init__(self, driver: WebDriver, url: str) -> None:
        """Initialize the page with a driver and a URL. It is assumed that the URL is valid."""
        self.driver = driver
        self.url = url
    
    def is_available(self) -> bool:
        """Return whether the page is available."""
        response = requests.get(self.url)
        if response.status_code in [200, 201] and "Page not found" in response.text:
            try:
                self.driver.get(self.url)
                return True
            except:
                return False
        return False