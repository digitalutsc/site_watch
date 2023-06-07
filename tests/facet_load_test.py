from tests.test import Test
from pages.collections_or_advanced_search_page import CollectionsOrAdvancedSearchPage

class FacetLoadTest(Test):
    def run(self, url: str, facet_type: str) -> None:
        collection_page = CollectionsOrAdvancedSearchPage(self.driver, url)
        if facet_type == "subject":
            assert collection_page.is_subject_facet_present(), "Subject facet is not present on collections page."
        elif facet_type == "genre":
            assert collection_page.is_genre_facet_present(), "Genre facet is not present on collections page."
        elif facet_type == "publication_date":
            assert collection_page.is_publication_date_facet_present(), "Publication date facet is not present on collections page."
        elif facet_type == "related_archival_fonds":
            assert collection_page.is_related_archival_fonds_facet_present(), "Related archival fonds facet is not present on collections page."
        else:
            raise ValueError(f"Invalid facet type: {facet_type}.")
