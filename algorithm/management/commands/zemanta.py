# -*- coding: utf-8 -*-
import urllib
import sys
import simplejson
import unicodedata
from algorithm.models import Algorithm, Tag
from pprint import pprint
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = u"""Update tags for all algorithms."""

    def handle(self, *args, **options):
        try:
            reload(sys)
            sys.setdefaultencoding("utf-8")
                
            algorithms = Algorithm.objects.all()
            for alg in algorithms:
                gateway = 'http://api.zemanta.com/services/rest/0.0/'
                args = {'method': 'zemanta.suggest',
                        'api_key': 'barhn7wrasi9e9l8ros5g9zy',
                        'text': ''+alg.description+'',
                        'return_rdf_links': '0',
                        'return_images': '0',
                        'markup_limit' : '0',
                        'articles_limit' : '0',
                        'format': 'json'}            
                args_enc = urllib.urlencode(args)
                
                raw_output = urllib.urlopen(gateway, args_enc).read()
                output = simplejson.loads(raw_output)
                keywords = output['keywords']
                for key in keywords:
                    if float(key['confidence']) > 0.1:
                        key_name = key['name'].encode('cp850','replace').decode('cp850')
                        try:
                            tag = Tag.objects.get(name=key_name)
                        except Tag.DoesNotExist:
                            tag = Tag(name=key_name)
                            tag.save() 
                       
                        alg.tags.add(tag)
                        alg.save()     
                        
                        #print alg_name +" : "+ key_name
                        
        except:
            import traceback
            traceback.print_exc()
            raise
