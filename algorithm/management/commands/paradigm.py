from django.core.management.base import BaseCommand
import json
from algorithm.controllers import *
import traceback

class Command(BaseCommand):
	help = u"""Peter Van Roy Paradigm Extraction"""

	def handle(self, *args, **options):
		try:		
			#["paradigm", "wpage", "abstract", "label"] 
			with open('paradigms.json', 'r') as jsonfile:
				paradigms = json.load(jsonfile)	
			for paradigm in paradigms['results']['bindings']:
				insert_paradigm(paradigm['label']['value'],paradigm['abstract']['value'],paradigm['wpage']['value'],paradigm['paradigm']['value'])
		except:
			traceback.print_exc()
			pass

