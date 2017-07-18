# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import traceback
import os
import pickle
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


class Command(BaseCommand):
    help = u"""Cria artefatos usados pela busca por documentos"""

    def handle(self, *args, **options):
        try:
            path_of_file = os.path.dirname(os.path.realpath(__file__))

            path_of_extractions = path_of_file + "/../../../extractor/temp/algorithms-txt"
            path_of_output = path_of_file + "/../../tfidf"

            document_list = []

            svd = TruncatedSVD(n_components=100, random_state=17)

            corpus = []
            for document in os.listdir(path_of_extractions):
                document_list.append(document[:-4])
                corpus.append("{}/{}".format(path_of_extractions, document))

            tf_idf_vectorizer = TfidfVectorizer(input='filename')

            tf_idf_matrix = tf_idf_vectorizer.fit_transform(corpus)

            tf_idf_transformed = svd.fit_transform(tf_idf_matrix)

            if not (os.path.isdir(path_of_output)):
                os.mkdir(path_of_output)

            documents_file_path = "{}/documents".format(path_of_output)
            documents_file = open(documents_file_path, 'w')
            pickle.dump(document_list, documents_file, pickle.HIGHEST_PROTOCOL)
            documents_file.close()

            terms_file_path = "{}/terms".format(path_of_output)
            terms_file = open(terms_file_path, 'w')
            pickle.dump(tf_idf_vectorizer.vocabulary_, terms_file, pickle.HIGHEST_PROTOCOL)
            terms_file.close()

            matrix_file_path = "{}/matrix".format(path_of_output)
            matrix_file = open(matrix_file_path, 'w')
            pickle.dump(tf_idf_transformed, matrix_file, pickle.HIGHEST_PROTOCOL)
            matrix_file.close()

            svd_components_file_path = "{}/svd_components".format(path_of_output)
            svd_components_file = open(svd_components_file_path, 'w', pickle.HIGHEST_PROTOCOL)
            pickle.dump(svd.components_, svd_components_file)
            svd_components_file.close()
        except:
            traceback.print_exc()
            pass
