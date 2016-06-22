# -*- coding: utf-8 -*-
from algorithm.models import Algorithm
from algorithm.controllers import *
from django.core.management.base import BaseCommand
import csv

#Código de implementação de lógica de geração de matriz de probabilidades desejáveis de ações dado o histórico do usuário.
#Contorna o problema da pontuação igual para ação feita repetidas vezes.
#A saída do programa é um arquivo csv salvo na pasta root do projeto com o nome 'matrizDesejavel.csv'.
class Command(BaseCommand):
    help = u"""Matriz desejável de comportamento"""

    def handle(self, *args, **options):
        try:
            with open('matrizDesejavel.csv', 'w') as csvfile:
                actions = ['state','aa', 'ai', 'v', 'ap']
                #writer para escrever cabeçalho da matriz
                writer = csv.DictWriter(csvfile, fieldnames=actions)
                writer.writeheader()

                #dicionário separado por ação contendo todos os usuários que fizeram cada ação pelo menos uma vez
                users_action = get_users_by_actions()
                #total de usuários do sistema
                n_users= get_n_users()
                #todas as combinações de ações possíveis para histórico
                historico = str_historico()

                for hist in historico:
                    rowResults = {}
                    rowResults['aa'] = 0
                    rowResults['ai'] = 0
                    rowResults['v'] = 0                        
                    rowResults['ap'] = 0

                    maxProb = 1

                    for acao in users_action.keys():
                        
                        totalOccurrences = hist.count(acao) 
                        rowResults[acao] = maxProb/float(totalOccurrences + 1)

                    writer.writerow({'state': hist,'aa': rowResults['aa'], 'ai': rowResults['ai'],'v': rowResults['v'],'ap': rowResults['ap']})

        except:
            import traceback
            traceback.print_exc()
            raise