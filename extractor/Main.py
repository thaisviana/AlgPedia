'''
Created on 20/02/2013

@author: Pericolo
'''

from DBPediaQueryFetcher import QueryFetcher
from FileWriters import TXTWriter
import os
from django.conf import settings
settings.configure(DEBUG=True)

#from extractor.models import Classification
import MySQLdb
import random

class ColumnExtractor:
	def __init__(self, file_name):
		self.file_name = file_name

	def extractColumn(self, column_index):
		F_H = open(self.file_name, 'r')

		lines = F_H.readlines()

		F_H.close()

		column = map(lambda x: x.split(',')[column_index], lines)

		return column

# http://live.dbpedia.org/page/Category:Algorithms -> pegar categorias dessa pagina e procurar infoboxes de codigo na wikipedia

def doMain():

	# if no second parameter is passed then the QueryFetcher assumes that there exists ./temp
	query_fetcher = QueryFetcher('csv')

	dbpedia_master_query = '''{
			?classification skos:broader <http://dbpedia.org/resource/Category:Algorithms>.
			?algorithm dct:subject ?classification.
			?algorithm foaf:isPrimaryTopicOf ?wikipedia
			}'''

	print "Calling QueryFetcher..."
	generated_file = query_fetcher.fetchResult(dbpedia_master_query)
	print generated_file

	print "Finished fetching results..."

	# always 0-based, baby
	insertClassifications(generated_file, 0)

# returns a list of beautiful names.
# each name only appears once in this list.
def extractClassificationNames(classif_list):

		beautiful_names = dict()

		names = map(lambda x: x.split(':')[2], classif_list)
		names = map(lambda x: x.replace('_', ' ').title(), names)

		for i in range(0, len(names)):
			beautiful_names[names[i]] = classif_list[i] if names[i] not in beautiful_names else None

		#for name in names:
		#	beautiful_names[name] = '' if name not in beautiful_names else None

		return beautiful_names

def extractURI(line):
	uri = line.split(';')[-1]
	return uri

def extractClassification(line):
	classification = line.split(':')[2]
	classification = classification.replace(';http', '')
	classification = classification.replace('_', ' ').title()
	return classification

def insertClassifications(filename, col_number):

	print filename
	print "Preparing extrated names for insertion..."

	col_extractor = ColumnExtractor(filename)

	col_classification = col_extractor.extractColumn(col_number)

	print "Connecting to database..."
	db = MySQLdb.connect("localhost","root","123mudar","AlgPedia" )
	cursor = db.cursor()

	for line in col_classification:
		classification = extractClassification(line)
		uri = extractURI(line)
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

if __name__ == '__main__':
    doMain();
