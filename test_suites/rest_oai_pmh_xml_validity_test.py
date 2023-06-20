from pages.rest_oai_pmh_xml_page import RestOAIPMHXMLPage
from test_suites.test import Test

class RestOAIPMHXMLValidityTest(Test):
    """ A test to check that the rest_oai_pmh_xml page is valid XML. """
    def run(self, url: str) -> None:
        rest_oai_pmh_xml_page = RestOAIPMHXMLPage(self.driver, url)
        assert rest_oai_pmh_xml_page.is_valid_xml(), "REST OAI PMH XML page is not valid XML."
