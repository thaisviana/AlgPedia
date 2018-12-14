
#encoding: utf-8

import os
from bs4 import BeautifulSoup
from django.conf import settings

class FileWriter():
    def __init__(self,params):
        pass

    def writeFile(self, text, file_name):
        pass

class HTMLWriter(FileWriter):
    def __init__(self, output_folder='./extractor/temp'):
        self.base_path = output_folder
        self.file_extension = 'html'

    def writeFile(self, text, file_name):
        file_path = os.path.join(self.base_path, file_name + '.' + self.file_extension)

        F_HANDLE = open(file_path, 'w')

        F_HANDLE.write(text)

        F_HANDLE.close()

        return file_path

    def updateOutputFolderPath(self, new_folder_path):
        self.base_path = new_folder_path

class CSVWriter(FileWriter):
    def __init__(self, output_folder='./extractor/temp'):
        self.base_path = os.path.abspath(output_folder)
        self.file_extension = 'csv'

    def writeFile(self, html, file_name):
        file_path = os.path.join(self.base_path, file_name + '.' + self.file_extension)
        file_converter = HTMLToCSV(html)
        F_HANDLE = open(file_path, 'w')
        iterator = iter(file_converter.convert())
        F_HANDLE.write(iterator.next())
        for item in iterator:
            F_HANDLE.write('\n')
            F_HANDLE.write(item)
        F_HANDLE.close()
        return file_path

    def appendFile(self, html, file_name):
        file_path = os.path.join(self.base_path, file_name + '.' + self.file_extension)

        file_converter = HTMLToCSV(html)

        #print file_path

        F_HANDLE = open(file_path, 'a')

        iterator = iter(file_converter.convert())

        F_HANDLE.write(iterator.next())

        for item in iterator:
            F_HANDLE.write('\n')
            F_HANDLE.write(item)

        F_HANDLE.close()

        return file_path

class TXTWriter(FileWriter):
    def __init__(self, output_folder='./extractor/temp'):
        self.base_path = os.path.abspath(output_folder)
        self.file_extension = 'txt'

    def writeLinesToFile(self, list, file_name):
        file_path = os.path.join(self.base_path, file_name + '.' + self.file_extension)

        F_HANDLE = open(file_path, 'w')

        list.sort()
        iterator = iter(list)

        F_HANDLE.write(iterator.next())

        for item in iterator:
            F_HANDLE.write('\n')
            F_HANDLE.write(item)

        F_HANDLE.close()

        return file_path

    def writeDictKeysToFile(self, dict, file_name):
        file_path = os.path.join(self.base_path, file_name + '.' + self.file_extension)

        F_HANDLE = open(file_path, 'w')

        keys = dict.keys()
        keys.sort()

        iterator = iter(keys)

        F_HANDLE.write(iterator.next())

        for item in iterator:
            F_HANDLE.write('\n')
            F_HANDLE.write(item)

        F_HANDLE.close()

        return file_path

    def writeDictValuesToFile(self, dict, file_name):
        file_path = os.path.join(self.base_path, file_name + '.' + self.file_extension)

        F_HANDLE = open(file_path, 'w')

        vals = dict.values()
        vals.sort()

        iterator = iter(vals)

        F_HANDLE.write(iterator.next())

        for item in iterator:
            F_HANDLE.write('\n')
            F_HANDLE.write(item)

        F_HANDLE.close()

        return file_path

class XMLWriter(FileWriter):
    def __init__(self, params):
        pass

class JSONWriter(FileWriter):
    def __init__(self, params):
        pass

# testar
class RDFWriter(FileWriter):
    def __init__(self, algorithm, file_name):
        self.algorithm = algorithm
        self.classification = algorithm.classification
        self.file_name = file_name
        self.RDF_variables = {}

    def set_file_name(self, file_name):
        self.file_name = file_name

    def generate_RDF_text(self):
        #path = os.path.join(os.path.dirname(__file__), '../algorithm/rdf/rdf_modelo.xml').replace('/','\\')

        self.RDF_variables['ALG_NAME'] = self.algorithm.name
        self.RDF_variables['ALG_ALGPEDIA_URI'] =  self.algorithm.get_show_url()
        self.RDF_variables['ALG_DBPEDIA_URI'] = self.algorithm.uri
        self.RDF_variables['ALG_ABOUT'] = self.algorithm.classification.name
        self.RDF_variables['ALG_CLASSIFICATION_NAME'] = self.classification.name

        alg_rdf_text = self.replace_vars_in_template(self.RDF_variables)

        return alg_rdf_text

    def replace_vars_in_template(self, variables):
        if settings.LOCAL:
            template_path = os.path.join(os.path.dirname(__file__), '../algorithm/static/rdf/rdf_modelo.xml').replace('/', '\\')
        else:
            template_path = os.path.join(os.path.dirname(__file__), '../algorithm/static/rdf/rdf_modelo.xml')
        rdf_template = open(template_path)
        lines = rdf_template.readlines()
        rdf_template.close()

        text = '\n'.join(lines)

        for variable, value in variables.iteritems():
            text = text.replace(variable, str(value))

        return text

    def create_rdf_file(self):
        rdf_text = self.generate_RDF_text()


        rdf_file = open(self.file_name, 'w')
        rdf_file.write(rdf_text)
        rdf_file.close()

        file_parts = self.file_name.split('/')
        file_name = '/'.join(file_parts[-2:])

        return file_name


# HTMLToXXX converter Classes
class HTMLToCSV:
    def __init__(self, html):
        self.html = html

    def convert(self):
        table = BeautifulSoup(self.html)
        converted = list()

        for row in table.findAll('tr'):
            aux = list()
            for col in row.findAll('td'):
                aux.append(col.string)
            line = ';'.join(aux)
            if(line != ''):
                converted.append(line.encode(encoding='UTF-8'))

        return converted

class HTMLToXML:
    pass

class HTMLToJSON:
    pass
