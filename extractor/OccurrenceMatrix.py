from WikiPediaExtractors import WikiPediaAbstractExtractor
import nltk

class OccurrenceMatrix:
    stop_words = ['.', '\'', '\"', ',', '(', ')', '[', ']' ';', '-', '{', '}']

    def __init__(self):
        pass

    def get_page_text(self, alg_url):
        wiki_alg_extractor = WikiPediaAbstractExtractor()

        wiki_alg_extractor.search_page(alg_url)
        return wiki_alg_extractor.get_full_text()

    def get_term_count(self, full_text):
        page_tokens = nltk.word_tokenize(full_text)

        page_terms = {}

        for token in page_tokens:
            token = token.lower()
            if token in OccurrenceMatrix.stop_words:
                continue

            if token in page_terms:
                page_terms[token]+= 1
            else:
                page_terms[token] = 1

        return page_terms

if __name__ == "__main__":
    occ_matrix = OccurrenceMatrix()
    alg_url = 'https://en.wikipedia.org/wiki/Insertion_sort'

    full_text = occ_matrix.get_page_text(alg_url)
    terms_dict = occ_matrix.get_term_count(full_text)

    print len(terms_dict)
