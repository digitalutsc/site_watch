from pages.page import BasePage
import requests


class RestOAIPMHXMLPage(BasePage):
    def is_valid_xml(self) -> bool:
        """Return whether the XML on the page is valid."""
        # There are two things that would make it invalid.
        #   - The page is unavailable as per `is_available()`
        #   - The XML on the page contains "idDoesNotExist" or "badVerb"
        if self.is_available():
            # Send a request to get the text
            response_text = requests.get(self.url).text
            if "idDoesNotExist" in response_text or "badVerb" in response_text:
                return False
            return True
        return False
