import os
import nltk
import math
import sys
import pickle
import numpy as np
import codecs
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

path_of_file = os.path.dirname(os.path.realpath(__file__))

path_of_extractions = path_of_file + "/../extractor/temp/algorithms-txt"
path_of_output = path_of_file + "/output/tfidf"

sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")

words_mapper = {}
documents_list = []
tf_matrix = []
tf_idf_matrix = []
document_counter = 0
idf_list = []

svd = TruncatedSVD(n_components=100, random_state=17)
tf_idf_transformed = None


def calc_idf():
    for word in words_mapper:
        df_term = 0
        term_frequency = tf_matrix[words_mapper[word]]
        for tf in term_frequency:
            if tf > 0:
                df_term += 1
        N = len(term_frequency)
        idf = math.log((N / df_term))
        idf_list.append(idf)


def calc_tfidf():
    global tf_idf_transformed

    calc_idf()
    for i in range(len(tf_matrix)):
        tf_idf_matrix.append([])
        for j in range(len(tf_matrix[i])):
            tf_idf = tf_matrix[i][j] * idf_list[i]
            tf_idf_matrix[i].append(tf_idf)

    np_tf_idf = np.matrix(tf_idf_matrix)
    tf_idf_transformed = svd.fit_transform(np_tf_idf.transpose())


for episode in os.listdir(path_of_extractions):
    document_counter += 1
    documents_list.append(episode)
    for term in tf_matrix:
        term.append(0)
    #text_file = open("{}/{}".format(path_of_extractions, episode))
    text_file = codecs.open("{}/{}".format(path_of_extractions, episode), encoding='utf-8')
    text = text_file.read()
    paragraphs = text.splitlines()
    for paragraph in paragraphs:
        sentences = sent_tokenizer.tokenize(paragraph)
        for sentence in sentences:
            if sentence.strip():
                words = nltk.word_tokenize(sentence)
                for word in words:
                    if word in words_mapper:
                        tf_matrix[words_mapper[word]][-1] += 1
                    else:
                        term_frequency = [0] * document_counter
                        words_mapper[word] = len(words_mapper)
                        term_frequency[-1] = 1
                        tf_matrix.append(term_frequency)
calc_tfidf()

if not (os.path.isdir(path_of_output)):
    os.mkdir(path_of_output)

documents_file_path = "{}/documents".format(path_of_output)
documents_file = open(documents_file_path, 'w')
pickle.dump(documents_list, documents_file, pickle.HIGHEST_PROTOCOL)
documents_file.close()

terms_file_path = "{}/terms".format(path_of_output)
terms_file = open(terms_file_path, 'w')
pickle.dump(words_mapper, terms_file, pickle.HIGHEST_PROTOCOL)
terms_file.close()

matrix_file_path = "{}/matrix".format(path_of_output)
matrix_file = open(matrix_file_path, 'w')
pickle.dump(tf_idf_transformed, matrix_file, pickle.HIGHEST_PROTOCOL)
matrix_file.close()

svd_components_file_path = "{}/svd_components".format(path_of_output)
svd_components_file = open(svd_components_file_path, 'w', pickle.HIGHEST_PROTOCOL)
pickle.dump(svd.components_, svd_components_file)
svd_components_file.close()
