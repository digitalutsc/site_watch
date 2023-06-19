from pages.collection_page import CollectionPage
from test_suites.test import Test

class OpenSeaDragonLoadTest(Test):
    """ A test to check that the openseadragon viewer loads on the collection page. """
    def run(self, url: str) -> None:
        collection_page = CollectionPage(self.driver, url)
        assert collection_page.is_openseadragon_loads(), "Openseadragon viewer does not load on collection page."

class MiradorLoadTest(Test):
    """ A test to check that the mirador viewer loads on the collection page. """
    def run(self, url: str) -> None:
        collection_page = CollectionPage(self.driver, url)
        assert collection_page.is_mirador_loads(), "Mirador viewer does not load on collection page."

class MiradorPageCountTest(Test):
    """ A test to check that the mirador viewer has the expected number of thumbnails."""
    def run(self, url: str, expected_number_of_thumbnails: int) -> None:
        collection_page = CollectionPage(self.driver, url)
        actual_number_of_thumbnails = collection_page.get_mirador_page_count()
        assert actual_number_of_thumbnails == expected_number_of_thumbnails, f"Mirador viewer does not have the expected number of thumbnails. Expected {expected_number_of_thumbnails}, got {actual_number_of_thumbnails}."

class AblePlayerLoadTest(Test):
    """ A test to check that the ableplayer viewer loads on the collection page. """
    def run(self, url: str) -> None:
        collection_page = CollectionPage(self.driver, url)
        assert collection_page.is_ableplayer_loads(), "Ableplayer viewer does not load on collection page."

class AblePlayerTranscriptLoadTest(Test):
    """ A test to check that the transcript of the ableplayer viewer loads on the collection page. """
    def run(self, url: str) -> None:
        collection_page = CollectionPage(self.driver, url)
        # First check that the ableplayer viewer loads
        assert collection_page.is_ableplayer_loads(), "Ableplayer viewer does not load on collection page."
        # Then check that the transcript loads
        assert collection_page.is_ableplayer_transcript_loads(), "Ableplayer transcript does not load on collection page."
