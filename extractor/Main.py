from DBPediaQueryFetcher import QueryFetcher
from ColumnExtractor import ColumnExtractor
from OccurrenceMatrixExtractor import OccurrenceMatrixExtractor
import os
from django.conf import settings
import MySQLdb
import random
import json

settings.configure(DEBUG=True)

ban_list = ["http://en.wikipedia.org/wiki/Eagle_strategy\n", "http://en.wikipedia.org/wiki/Reactive_search_optimization\n", "http://en.wikipedia.org/wiki/List_of_regular_expression_software\n", "http://en.wikipedia.org/wiki/FSA-Red_Algorithm\n"]

# http://live.dbpedia.org/page/Category:Algorithms -> pegar categorias dessa pagina e procurar infoboxes de codigo na wikipedia

# returns a list of beautiful names.
# each name only appears once in this list.
def extract_classification_names(classif_list):
    beautiful_names = dict()

    names = map(lambda x: x.split(':')[2], classif_list)
    names = map(lambda x: x.replace('_', ' ').title(), names)

    for i in range(0, len(names)):
        beautiful_names[names[i]] = classif_list[i] if names[i] not in beautiful_names else None

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
    db = MySQLdb.connect("localhost", "root", "123mudar", "AlgPedia")
    cursor = db.cursor()

    for line in col_classification:
        classification = extract_classification(line)
        uri = extract_URI(line)
        print "Inserting ", classification, uri
        try:
            query = "INSERT INTO algorithm_classification VALUES (%s,%s,%s)"
            print "Executing: ", query

            # this id should be a uuid
            # cursor.execute(query,(str(uuid.uuid4()),classification,uri))
            cursor.execute(query, (random.randint(1, 10000000), classification, uri))
            db.commit()
        except MySQLdb.Error as error:
            print "Error: {}".format(error)
            # print "Insert failed, rollback"
            db.rollback()
    db.close()


def create_directory(path):
    if not (os.path.isdir(path)):
        os.mkdir(path)


def save_alg_text_on_file(alg_name, alg_dict):
    alg_path = 'temp/algorithms/'
    print "Saving JSON for", alg_name
    create_directory(alg_path)

    with open(alg_path + alg_name + '.json', 'w') as f:
        json.dump(alg_dict, f, indent=4)


def insert_algorithms(filename):
    col_number_dbpedia = 1
    col_number_wikipedia = 2

    col_extractor = ColumnExtractor(filename)

    col_alg_url_wikipedia = col_extractor.extractColumn(col_number_wikipedia)
    col_alg_url_dbpedia = col_extractor.extractColumn(col_number_dbpedia)

    occ_matrix_extractor = OccurrenceMatrixExtractor()

    alg_dict = {}
    for alg_url in col_alg_url_wikipedia:
        if alg_url not in ban_list:
            page_info = occ_matrix_extractor.get_page_text(alg_url)

            full_text = {'about': page_info[2], 'full_text': page_info[1], 'wikipedia_url': alg_url}
            alg_dict[page_info[0].replace("_", " ").strip().title()] = full_text

    for alg_dbpedia_url in col_alg_url_dbpedia:
        start = alg_dbpedia_url.index("http://dbpedia.org/resource/") + len("http://dbpedia.org/resource/")
        alg_name = alg_dbpedia_url[start:].replace("_", " ").strip().title()

        if alg_name in alg_dict.keys():
            alg_dict[alg_name]['dbpedia_url'] = alg_dbpedia_url

    for alg_name in alg_dict.keys():
        save_alg_text_on_file(alg_name, alg_dict[alg_name])


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

    # generated_file = extract(dbpedia_master_query, "algorithms")
    #
    # insert_algorithms(generated_file)
    insert_algorithms("temp/dbpedia_algorithms_fetch_0.csv")

def doMain():
    print "Extracting classifications"
    # extract_classifications()

    print "Extracting algorithms"
    extract_algorithms()


if __name__ == '__main__':
    doMain()
