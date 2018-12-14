'''
Created on 26/02/2013

@author: Pericolo
'''
import os
import requests
import urllib
from .FileWriters import  HTMLWriter, CSVWriter
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
        response = requests.get(self.base_url,data, headers)
        # response = urllib2.urlopen(request)

        return response.json()

    def fetchCount(self, query_body):
        query_string = "select count(*) where " + query_body

        result = self.fetch(query_string)

        soup = BeautifulSoup(result)
        pre = soup('pre')
        return int(pre[0].string)

    # fetch the resource and delegate the writing of the file to the
    # appropriate instance of FileWriter
    def fetchResult(self, query_body, name):
        query = "select * where " + query_body
        the_page = self.fetch(query)
        file_path = self.file_writer.writeFile(the_page, 'dbpedia_{}_fetch_{}'.format(name, self.n_fetch))
        return file_path

    # change the output path of the fetched resource
    def changeOutputFolder(self, new_folder_path):
        self.temp_folder = new_folder_path
        self.file_writer.updateOutputFolderPath(new_folder_path)
