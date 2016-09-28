# -*- coding: utf-8 -*-
from algorithm.controllers import *
from django.core.management.base import BaseCommand
import csv

"""Código de implementação de lógica de geração de matriz de probabilidades de ações dado o histórico do usuário.
#O cálculo das probabilidades é feito usando-se funções de obtenção de total de usuários que realizaram tal ação e
#usando a fórmula do teorema de Bayes. Probabilidades de ações dado históricos que contém a ação que será efetuada estão sendo ignoradas
#temporariamente devido à alteração feita no banco de dados.
#A saída do programa é um arquivo csv salvo na pasta root do projeto com o nome 'matriz.csv'. """
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
                            ##### CONTAGEM DE USUÁRIOS QUE FIZERAM TODAS AS AÇÕES DO HISTÓRICO QUE SÃO DIFERENTES DA AÇÃO A SER CALCULADA A PROB
                             
                            '''For para montar a lista sem repetições de usuários que fizeram as ações do histórico que não são a 
                            ação futura '''
                            totalActionsHist = len(hist.split('_'))
                            usersHistNoRepetition = []
                            
                            for index in range(len(hist.split('_'))):
                                if hist.split('_')[index] == acao: pass
                                else: usersHistNoRepetition = list(set(filter(lambda x: x in users_action[hist.split('_')[index]]  , usersHistNoRepetition)))
                            
                            #### CONTAGEM DE USUÁRIO QUE FIZERAM AÇÃO REPETIDAS VEZES NO HISTÓRICO
                            '''Lista contendo os usuários que fizeram ação tantas vezes quanto aparece no histórico'''
                            totalActionRepetitionHist = hist.count(acao)
                            usersHistRepetition = list(set(filter(lambda x: users_action[acao].count(x) == totalActionRepetitionHist, users_action[acao])))
                            
                            '''Lista contendo os usuários que fizeram ação tantas vezes quanto aparece no histórico + 1 (que seria
                                a ação futura)'''
                            totalActionRepetition = totalActionRepetitionHist + 1
                            usersTotalRepetition = list(set(filter(lambda x: users_action[acao].count(x) == totalActionRepetition, users_action[acao])))
                            
                            '''Lista com todos os usuários que fizeram todas as ações do histórico'''
                            usersHist = usersHistNoRepetition + usersHistRepetition
                            
                            '''Lista com todos os usuários que fizeram todas as ações do histórico e a ação futura'''
                            usersHistAndAction = usersTotalRepetition + usersHistNoRepetition
                            
                            bayes = len(usersHistAndAction)/ float(len(usersHist))
                            rowResults[acao] = bayes
                    writer.writerow({'state': hist,'aa': rowResults['aa'], 'ai': rowResults['ai'],'v': rowResults['v'],'ap': rowResults['ap']})

                            
                
        except:
            import traceback
            traceback.print_exc()
            raise