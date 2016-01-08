# -*- coding: utf-8 -*-
from algorithm.models import Algorithm
from algorithm.controllers import *
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    help = u"""Matrix de analise de comportamento"""

    def handle(self, *args, **options):
        try:
            with open('matrix.csv', 'w') as csvfile:
                prob_actions = ['state','aa', 'ai', 'v', 'ap']
                writer = csv.DictWriter(csvfile, fieldnames=prob_actions)

                writer.writeheader()
                writer.writerow({'state': 'none','aa': prob_aa(), 'ai': prob_ai(),'v': prob_v(),'ap':prob_ap() })
        except:
            import traceback
            traceback.print_exc()
            raise