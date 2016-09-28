'''
Created on 26/02/2013

@author: Pericolo
'''
import os
import urllib
import urllib2
from FileWriters import HTMLWriter, CSVWriter
from bs4 import *

class QueryFetcher:

    def __init__(self, fetch_format, temp_folder=os.path.abspath('./temp')):

		self.n_fetch = 0
		self.temp_folder = temp_folder
		self.base_url = 'http://dbpedia.org/sparql'

		self.get_params = {
			  'query' : '',
			  'default-graph-uri' : 'http://dbpedia.org',
			  'format'  : 'text/html',
			  'timeout' : 0,
			  'debug' : 'on'
		}

		# Creating the appropriate type of writer
		if(fetch_format.upper() == 'HTML'):
			self.file_writer = HTMLWriter(self.temp_folder)
		elif(fetch_format.upper() == 'CSV'):
			self.file_writer = CSVWriter(self.temp_folder)

    def fetch(self, query):
        self.get_params['query'] = query

        query_url = self.base_url + '?' + urllib.urlencode(self.get_params)

        data = urllib.urlencode(self.get_params)
        headers = {'User-Agent' : 'Mozilla/5.0'}
        request = urllib2.Request(self.base_url,data, headers)
        response = urllib2.urlopen(request)

        return response.read()

    def fetchCount(self, query_body):
        query_string = "select count(*) where " + query_body

        result = self.fetch(query_string)

        soup = BeautifulSoup(result)
        pre = soup('pre')
        return int(pre[0].string)

    # fetch the resource and delegate the writing of the file to the
    # appropriate instance of FileWriter
    def fetchResult(self, query_body):
        file_paths = []
        batch_size = 100
        total_results = self.fetchCount(query_body)

        offset = 0

        while offset*batch_size < total_results:
    		query = "select * where " + query_body
    		query += "limit " + str(batch_size) + " offset "
    		query += str(offset*batch_size)
    		# print query

    		self.get_params['query'] = query

    		the_page = self.fetch(query)

    		file_paths.append(self.file_writer.writeFile(the_page, 'dbpedia_fetch_%d' % self.n_fetch))

    		offset += 1
    		query = query_body

    		print str(offset*batch_size) + " results fetched"
    		print str(total_results - offset*batch_size) + " left to fetch"

    		self.n_fetch += 1

    	return file_paths

    # change the output path of the fetched resource
    def changeOutputFolder(self, new_folder_path):
        self.temp_folder = new_folder_path
        self.file_writer.updateOutputFolderPath(new_folder_path)
