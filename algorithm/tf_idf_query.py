import os
import nltk
import sys
import pickle
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity


path_of_file = os.path.dirname(os.path.realpath(__file__))

path_of_tfidf_output = path_of_file + "/tfidf"

words_mapper = None
documents_list = None
svd_components = None
tf_idf_transformed = None

def score(sentence):
    words = nltk.word_tokenize(sentence)

    query_tf = np.array([0]*len(words_mapper))

    for w in words:
        if w in words_mapper:
            query_tf[words_mapper[w]] += 1

    query_tf_transformed = np.matmul(svd_components, query_tf.reshape(-1,1)).transpose()
    score_list = cosine_similarity(query_tf_transformed, tf_idf_transformed)[0]

    return score_list

def query(sentence):
    score_list = score(sentence)

    sorted_score_list = sorted(documents_list, key=lambda x: score_list[documents_list.index(x)], reverse=True)[:5]

    return sorted_score_list

def load_documents():
    global documents_list

    documents_file = open("{}/documents".format(path_of_tfidf_output))
    documents_list = pickle.load(documents_file)
    documents_file.close()

def load_terms():
    global words_mapper

    terms_file = open("{}/terms".format(path_of_tfidf_output))
    words_mapper = pickle.load(terms_file)
    terms_file.close()

def load_svd():
    global tf_idf_transformed
    global svd_components

    #tf_idf_file = open("{}/tfidf".format(path_of_tfidf_output))
    #tf_idf_matrix = pickle.load(tf_idf_file)
    #tf_idf_file.close()

    #svd = TruncatedSVD(n_components=100, random_state=17)
    #tf_idf_transformed = svd.fit_transform(tf_idf_matrix.transpose())
    #svd_components = svd.components_

    matrix_file = open("{}/matrix".format(path_of_tfidf_output))
    tf_idf_transformed = pickle.load(matrix_file)
    matrix_file.close()

    svd_components_file = open("{}/svd_components".format(path_of_tfidf_output))
    svd_components = pickle.load(svd_components_file)
    svd_components_file.close()

##### MAIN #####

#Load artifacts
load_documents()
load_terms()
load_svd()

#Ask for input
while True:
    n = raw_input("Digite a string para ser pesquisada ou exit para sair: ")
    if n == "exit":
        break
    else:
        print query(n)
