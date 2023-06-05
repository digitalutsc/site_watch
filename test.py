from selenium.webdriver.remote.webdriver import WebDriver
from page import *
from typing import Any

class Test():
    """ An Abstract Base Class for tests. """
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver