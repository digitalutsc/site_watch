from selenium.webdriver.remote.webdriver import WebDriver


class Test():
    """ An Abstract Base Class for tests. """
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
