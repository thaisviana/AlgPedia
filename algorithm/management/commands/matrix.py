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

                users_action = get_users_by_actions()
                print users_action
                n_users= get_n_users()
                
                historico = str_historico()

                for acao in users_action.keys():
                    for h_posicao in historico:
                        if (acao not in h_posicao):
                            if h_posicao is '':
                                print acao, len(users_action[acao])/n_users
                            elif len(h_posicao.split('_')) == 1 :
                                subset_acao = list(set(filter(lambda x: x in users_action[acao] , users_action[h_posicao])))
                                print acao, h_posicao, len(subset_acao)/float(len(users_action[h_posicao]))
                            else :
                                subset = users_action[h_posicao.split('_')[0]]
                                for index in range(len(h_posicao.split('_'))):
                                    if index == 0: pass
                                    subset = list(set(filter(lambda x: x in users_action[h_posicao.split('_')[index]] , subset)))
                                subset_acao = list(set(filter(lambda x: x in users_action[acao] , subset)))
                                print acao, h_posicao, len(subset_acao)/float(len(subset))                           

                            
                #writer.writerow({'state': 'none','aa': len(users_action['aa'].values)/n_users, 'ai': prob_ai(),'v': prob_v(),'ap':prob_ap() })
        except:
            import traceback
            traceback.print_exc()
            raise