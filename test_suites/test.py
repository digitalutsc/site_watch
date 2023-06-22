"""
This module contains the Test class, which is a base class for all tests.
"""

from selenium.webdriver.remote.webdriver import WebDriver


class Test():
    """ 
    An Abstract Base Class for tests.
    """
    driver: WebDriver  # The driver used to load the page

    def __init__(self, driver: WebDriver) -> None:
        """ Create a new Test object with the given driver. """
        self.driver = driver
