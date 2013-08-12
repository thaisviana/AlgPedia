'''
Created on 01/03/2013

@author: Pericolo
'''

import os
from extractor.FileWriters import TXTWriter
from extractor.Extractor import CSVColumnExtractor
from extractor.DBPediaQueryFetcher import QueryFetcher
from algorithm.models import Classification
from algorithm.controllers import *

from extractor.WikiPediaExtractors import WikiPediaAbstractExtractor

class Bootstrapper():
	def __init__(self):
		pass
	
	def doDatabaseImporting(self):
		query_fetcher = QueryFetcher('csv')
		dbpedia_master_query = '''select * where{
			?classification skos:broader <http://dbpedia.org/resource/Category:Algorithms>.
			?algorithm dcterms:subject ?classification.
			?algorithm foaf:isPrimaryTopicOf ?wikipedia
			}'''

		filename = query_fetcher.fetchResult(dbpedia_master_query)
		
		# always 0-based, baby
		#self.insertClassifications(filename, 0)
		
		# second parameter is a list of columns that will be used create the classification object
		#self.insert_classifications(filename, [0])
		self.populate_database(filename, [0,1,2])
		
	# second parameter is a list of columns that will be used to populate the database
	def populate_database(self, filename, cols):
		col_extractor = CSVColumnExtractor(filename)
		
		class_alg_mapping = zip(col_extractor.extract_column(cols[0]), col_extractor.extract_column(cols[1]), col_extractor.extract_column(cols[2]))
		
		for mapping in class_alg_mapping:
			#print mapping[0]
			#if mapping[0].split(':')[-1] == 'Sorting_algorithms':
			classif = self.insert_classification(mapping[0])
			#alg = self.insert_algorithm(mapping[1], classif)
			alg = self.insert_algorithm_conditional(mapping[2], mapping[1], classif)
		
	def insert_classification(self, classif_url):
		(name, uri) = self.extract_name_uri(classif_url)
		print name + ': ' + uri
		
		classif = insert_classification_db(name, uri)

		return classif
		
	def insert_algorithm_conditional(self, alg_url, alg_uri, classif):
		try:
			wiki_alg_extractor = WikiPediaAbstractExtractor()
			
			wiki_alg_extractor.search_page(alg_url)
			
			about = wiki_alg_extractor.get_alg_about()
			
			name = wiki_alg_extractor.get_alg_name()
			
			# returns a tuple (language, implementation_source)
			en_implementations = wiki_alg_extractor.get_alg_pseudo_code()
			
			# returns a tuple (language, implementation_source)
			implementations = wiki_alg_extractor.get_alg_implementations()
			
			if not en_implementations and not implementations:
				# this covers having neither a PT page nor a pseudocode	
				print "No implementation or pseudo for this algorithm.\n"
				return None
				
			alg = insert_algorithm_db(name, about, classif, alg_uri, True)	
			
			if en_implementations:
				for en_implementation in en_implementations:
					implementation = insert_implementation_db(alg, en_implementation[0], en_implementation[1],True)
					
			if implementations:
				for implementation in implementations:
					implementation = insert_implementation_db(alg,  implementation[0], implementation[1],True)			
					
			#will never be returned
			return None 
		except Exception, e:
			print e
			return None
			
	def insert_algorithm(self, alg_url, classif):
		try:
			wiki_alg_extractor = WikiPediaAbstractExtractor()
			
			wiki_alg_extractor.search_page(alg_url)
			
			about = wiki_alg_extractor.get_alg_about()
			
			name = wiki_alg_extractor.get_alg_name()
			
			alg = insert_algorithm_db(name, about, classif, True)
			
			# returns a tuple (language, implementation_source)
			pseudos = wiki_alg_extractor.get_pseudo_code()
			
			# returns a tuple (language, implementation_source)
			implementations = wiki_alg_extractor.get_alg_implementations()
			
			# deletes the added alg if it 
			if not pseudos and not implementations:
				# this covers having neither a PT page nor a pseudocode
				delete_algorithm_db(alg)
				return None
				
			if pseudo:
				for pseudo in pseudos:
					implementation = insert_implementation_db(alg, pseudo[0], pseudo[1], True)
					
			if implementations:
				for implementation in implementations:
					implementation = insert_implementation_db(alg,  implementation[0], implementation[1], True)			
					
			#will never be returned
			return None 
		except Exception, e:
			print e
			return None
		
	def extract_name_uri(self, classif_uri):
		name = classif_uri.split(':')[-1]
		name = name.replace('_',' ')
		name = name.title()
		
		return (name, classif_uri)
		
	def insert_classifications(self, filename, cols):
		col_extractor = ColumnExtractor(filename)
		
		col_classification = col_extractor.extractColumn(cols[0])
		
		(names, uris) = self.extract_names(col_classification)
		
		names, uris = (list(t) for t in zip(*sorted(zip(names,uris))))
		
		classifications = [{'name' : t[0], 'uris' : t[1]} for t in zip(names, uris)]
		
		for classification in classifications:
			aux_classification = Classification(name=classification['name'], uri=classification['uris'])
			aux_classification.save()
		
	def extract_names(self, classif_list):

		beautiful_names = dict()
		
		names = map(lambda x: x.split(':')[-1], classif_list)
		names = map(lambda x: x.replace('_', ' ').title(), names)
		
		for i in range(0, len(names)):
			#print "Key: " + str(names[i]) + " Value: " + classif_list[i]
			
			if(names[i] not in beautiful_names):
				beautiful_names[names[i]] = classif_list[i]	
		return (beautiful_names.keys(), beautiful_names.values())		
	
	# deprecated!!
	def insertClassifications(self, filename, col_number):
	
		col_extractor = ColumnExtractor(filename)
		
		col_classification = col_extractor.extractColumn(col_number)
		
		classif_names = self.extractNames(col_classification)
			
		txt_Writer = TXTWriter()
		
		file_name = txt_Writer.writeDictKeysToFile(classif_names, 'classifications')
		
		for key, val in classif_names.iteritems():
			#print str(key) + ': ' + str(val)
			aux_classification = Classification(name=key, uri=val)
			aux_classification.save()
	
	# deprecated!!
	# returns a list of beautiful names.	
	# each name only appears once in this list.
	def extractNames(self, classif_list):

		beautiful_names = dict()
		
		names = map(lambda x: x.split(':')[-1], classif_list)
		names = map(lambda x: x.replace('_', ' ').title(), names)
		
		for i in range(0, len(names)):
			#print "Key: " + str(names[i]) + " Value: " + classif_list[i]
			
			if(names[i] not in beautiful_names):
				beautiful_names[names[i]] = classif_list[i]	
		return beautiful_names
		#return (beautiful_names.keys(), beautiful_names.values())
		