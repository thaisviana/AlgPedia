'''
Created on 20/02/2013

@author: Pericolo
'''

from DBPediaQueryFetcher import QueryFetcher
from FileWriters import TXTWriter
import os

from algorithm.models import Classification



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

	dbpedia_master_query = '''select * where{
	?classification skos:broader <http://dbpedia.org/resource/Category:Algorithms>.
	?algorithm dcterms:subject ?classification.
	?algorithm foaf:isPrimaryTopicOf ?wikipedia
	}'''

	filename = query_fetcher.fetchResult(dbpedia_master_query)
	
	
	# always 0-based, baby
	insertClassifications(filename, 0)

# returns a list of beautiful names.	
# each name only appears once in this list.
def extractNames(classif_list):

		beautiful_names = dict()
		
		names = map(lambda x: x.split(':')[-1], classif_list)
		names = map(lambda x: x.replace('_', ' ').title(), names)
		
		for i in range(0, len(names)):
			beautiful_names[names[i]] = classif_list[i] if names[i] not in beautiful_names else None
		
		#for name in names:
		#	beautiful_names[name] = '' if name not in beautiful_names else None		
			
		return beautiful_names
	
def insertClassifications(filename, col_number):

	print filename
	
	col_extractor = ColumnExtractor(filename)
	
	col_classification = col_extractor.extractColumn(col_number)
	
	classif_names = extractNames(col_classification)
		
	txt_Writer = TXTWriter('./')
	
	file_name = txt_Writer.writeDictKeysToFile(classif_names, 'classif')
	
	for key, val in classif_names.iteritems():
		aux_classification = Classification(name=key, uri=val)
		aux_classification.save()
	
	

if __name__ == '__main__':
    doMain();