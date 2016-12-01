from WikiPediaExtractors import WikiPediaAbstractExtractor
import nltk
import MySQLdb

class OccurrenceMatrixExtractor:
    def __init__(self):
        pass

    def get_page_text(self, alg_url):
        wiki_alg_extractor = WikiPediaAbstractExtractor()

        wiki_alg_extractor.search_page(alg_url)
        return (wiki_alg_extractor.get_alg_name(), wiki_alg_extractor.get_full_text(), wiki_alg_extractor.get_alg_about())

    def insert_text(self, alg_name, full_text, id):
        print "Connecting to database..."
    	db = MySQLdb.connect("localhost","root","123mudar","AlgPedia" )
    	cursor = db.cursor()

        print "Inserting ", alg_name
        try:
            query = "INSERT INTO algorithm_algorithmfulltext VALUES (%s,%s,%s)"
            cursor.execute(query,(id, alg_name, full_text))
            db.commit()

        except MySQLdb.Error as error:
            print "Error: {}".format(error)
            print "Insert failed, rollingback"
            db.rollback()
	    db.close()

	return None
