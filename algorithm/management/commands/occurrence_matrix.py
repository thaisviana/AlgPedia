# -*- coding: utf-8 -*-
from algorithm.controllers import *
from django.core.management.base import BaseCommand
from algorithm.models import AlgorithmFullText
import nltk
import traceback
from collections import defaultdict
from algorithm.preprocessing import preProcessing

class Command(BaseCommand):
    help = u"""Occurence Matrix generator"""

    def generate_matrix(self, dicts):
        matrix = defaultdict(int)
        clean_matrix = defaultdict(int)
        for d in dicts:
            for k, v in d.items():
                matrix[k] += v
        for k in matrix.keys():
            if matrix[k] > 2:
                clean_matrix[k] = matrix[k]
        return clean_matrix

    def get_count_list(self):
        all_descriptions = AlgorithmFullText.objects.all()
        count_list = []
        for alg_description in all_descriptions:
            description_dict = preProcessing(alg_description.description)
            count_list.append((alg_description.alg_name, description_dict))

        return count_list

    def handle(self, *args, **options):
        try:
            dicts = self.get_count_list()
            # matrix = self.generate_matrix([d[1] for d in dicts])
            # print matrix
        except:
            traceback.print_exc()
            pass
