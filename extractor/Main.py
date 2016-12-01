from DBPediaQueryFetcher import QueryFetcher
from ColumnExtractor import ColumnExtractor
from FileWriters import TXTWriter
from OccurrenceMatrixExtractor import OccurrenceMatrixExtractor
import os
from django.conf import settings
settings.configure(DEBUG=True)

#from extractor.models import Classification
import MySQLdb
import random

# http://live.dbpedia.org/page/Category:Algorithms -> pegar categorias dessa pagina e procurar infoboxes de codigo na wikipedia

# returns a list of beautiful names.
# each name only appears once in this list.
def extract_classification_names(classif_list):

		beautiful_names = dict()

		names = map(lambda x: x.split(':')[2], classif_list)
		names = map(lambda x: x.replace('_', ' ').title(), names)

		for i in range(0, len(names)):
			beautiful_names[names[i]] = classif_list[i] if names[i] not in beautiful_names else None

		#for name in names:
		#	beautiful_names[name] = '' if name not in beautiful_names else None

		return beautiful_names

def extract_URI(line):
	uri = line.split(';')[-1]
	return uri

def extract_classification(line):
	classification = line.split(':')[2]
	classification = classification.replace(';http', '')
	classification = classification.replace('_', ' ').title()
	return classification

def insert_classifications(filename):
	col_number = 0
	print filename
	print "Preparing extrated names for insertion..."

	col_extractor = ColumnExtractor(filename)

	col_classification = col_extractor.extractColumn(col_number)

	print "Connecting to database..."
	db = MySQLdb.connect("localhost","root","123mudar","AlgPedia" )
	cursor = db.cursor()

	for line in col_classification:
		classification = extract_classification(line)
		uri = extract_URI(line)
		print "Inserting ", classification, uri
		try:
			query = "INSERT INTO algorithm_classification VALUES (%s,%s,%s)"
			print "Executing: ", query

			#this id should be a uuid
			#cursor.execute(query,(str(uuid.uuid4()),classification,uri))
			cursor.execute(query,(random.randint(1, 10000000),classification,uri))
			db.commit()
		except MySQLdb.Error as error:
			print "Error: {}".format(error)
			#print "Insert failed, rollback"
			db.rollback()
	db.close()

def create_directory(path):
    if not (os.path.isdir(path)):
		os.mkdir(path)

def save_alg_text_on_file(alg_name, alg_full_text):
	alg_path = 'temp/algorithms'
	create_directory(alg_path)
	with open(alg_path + '/' + alg_name + '.txt', 'w') as f:
		f.write(alg_full_text.encode('utf-8'))
		f.close()
	return None

def insert_algorithms(filename):
	col_number = 2
	alg_id = 1
	col_extractor = ColumnExtractor(filename)

	col_alg_url = col_extractor.extractColumn(col_number)

	occ_matrix_extractor = OccurrenceMatrixExtractor()

	for alg_url in col_alg_url:
		try:
			page_info = occ_matrix_extractor.get_page_text(alg_url)

			full_text = 'ABOUT\n' + page_info[2] + '\nFULL TEXT\n' + page_info[1]

			save_file = save_alg_text_on_file(page_info[0], full_text)
			save_db = occ_matrix_extractor.insert_text(page_info[0], page_info[1], alg_id) #Nao garante que todos os textos sao inseridos, teremos que inserir no banco depois de salvar nos arquivos.
			alg_id = alg_id + 1
		except Exception as e:
			pass

def extract(query, name):
	query_fetcher = QueryFetcher('csv')

	print "Calling QueryFetcher..."
	generated_file = query_fetcher.fetchResult(query, name)

	print "Finished fetching results..."

	return generated_file

def extract_classifications():
	dbpedia_master_query = '''{
			?classification skos:broader <http://dbpedia.org/resource/Category:Algorithms>.
			}'''

	generated_file = extract(dbpedia_master_query, "classifications")

	insert_classifications(generated_file)

def extract_algorithms():
	dbpedia_master_query = '''{
			?classification skos:broader <http://dbpedia.org/resource/Category:Algorithms>.
			?algorithm dct:subject ?classification.
			?algorithm foaf:isPrimaryTopicOf ?wikipedia
			}'''

	generated_file = extract(dbpedia_master_query, "algorithms")

	insert_algorithms(generated_file)

def doMain():
	print "Extracting classifications"
	#extract_classifications()

	print "Extracting algorithms"
	extract_algorithms()

if __name__ == '__main__':
    doMain();
