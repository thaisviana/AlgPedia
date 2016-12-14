# -*- coding: utf-8 -*-
from algorithm.controllers import *
from django.core.management.base import BaseCommand
from algorithm.models import Algorithm
import traceback


class Command(BaseCommand):
    help = u"""Occurence Matrix generator"""

    def handle(self, *args, **options):
        try:
            algorithms = self.get_algorithms()
            self.update_algorithm(algorithms)
            self.update_wikipedia(algorithms)

            classifications = self.get_classifications()
            self.update_classifications(classifications)

        except:
            traceback.print_exc()
            pass
