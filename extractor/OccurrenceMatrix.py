from WikiPediaExtractors import WikiPediaAbstractExtractor
import MySQLdb

class OccurrenceMatrixExtractor:
    def __init__(self):
        pass

    def get_page_text(self, alg_url):
        wiki_alg_extractor = WikiPediaAbstractExtractor()
        wiki_alg_extractor.search_page(alg_url)
        return wiki_alg_extractor.get_full_text()

    
