# -*- coding: utf-8 -*-
from algorithm.models import Algorithm
from algorithm.controllers import *
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    help = u"""Matriz de analise de comportamento"""

    def handle(self, *args, **options):
        try:
            with open('matriz.csv', 'w') as csvfile:
                prob_actions = ['state','aa', 'ai', 'v', 'ap']
                writer = csv.DictWriter(csvfile, fieldnames=prob_actions)
                writer.writeheader()
                users_action = get_users_by_actions()
                n_users= get_n_users()
                
                historico = str_historico()

                for hist in historico:
                    rowResults = {}
                    rowResults['aa'] = 0
                    rowResults['ai'] = 0
                    rowResults['v'] = 0                        
                    rowResults['ap'] = 0

                    for acao in users_action.keys():
                        if (acao not in hist):
                            if hist is '':
                                bayes = len(users_action[acao])/n_users
                                rowResults[acao] = bayes
                                #print acao, bayes
                            elif len(hist.split('_')) == 1 :
                                subset_acao = list(set(filter(lambda x: x in users_action[acao] , users_action[hist])))
                                bayes = len(subset_acao)/float(len(users_action[hist]))
                                rowResults[acao] = bayes
                                #print acao, hist, bayes
                            else :
                                subset = users_action[hist.split('_')[0]]
                                for index in range(len(hist.split('_'))):
                                    if index == 0: pass
                                    subset = list(set(filter(lambda x: x in users_action[hist.split('_')[index]] , subset)))
                                subset_acao = list(set(filter(lambda x: x in users_action[acao] , subset)))
                                bayes = len(subset_acao)/float(len(subset))
                                rowResults[acao] = bayes
                                #print acao, hist, bayes
                        else : 
                            rowResults[acao] = '-'
                    writer.writerow({'state': hist,'aa': rowResults['aa'], 'ai': rowResults['ai'],'v': rowResults['v'],'ap': rowResults['ap']})

                            
                
        except:
            import traceback
            traceback.print_exc()
            raise