# -*- coding: utf-8 -*-
from algorithm.models import Algorithm
from algorithm.controllers import *
from django.core.management.base import BaseCommand
import csv

#Código de implementação de lógica de geração de matriz de probabilidades de ações dado o histórico do usuário.
#O cálculo das probabilidades é feito usando-se funções de obtenção de total de usuários que realizaram tal ação e
#usando a fórmula do teorema de Bayes. Probabilidades de ações dado históricos que contém a ação que será efetuada estão sendo ignoradas
#temporariamente devido à alteração feita no banco de dados.
#A saída do programa é um arquivo csv salvo na pasta root do projeto com o nome 'matriz.csv'.
class Command(BaseCommand):
    help = u"""Matriz de analise de comportamento"""

    def handle(self, *args, **options):
        try:
            with open('matriz.csv', 'w') as csvfile:
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

                    for acao in users_action.keys():
                        if (acao not in hist):
                            if hist is '':
                                bayes = len(users_action[acao])/n_users
                                rowResults[acao] = bayes

                            elif len(hist.split('_')) == 1 :
                                usersActionAndHist = list(set(filter(lambda x: x in users_action[acao] , users_action[hist])))
                                usersHist = users_action[hist]

                                bayes = len(usersActionAndHist)/float(len(usersHist))

                                rowResults[acao] = bayes
                                
                            else :
                                #inicializa com todos os usuários que fizeram a primeira ação
                                usersHist = users_action[hist.split('_')[0]]
                                for index in range(len(hist.split('_'))):
                                    if index == 0: pass
                                    usersHist = list(set(filter(lambda x: x in users_action[hist.split('_')[index]] , usersHist)))
                                
                                usersAction = users_action[acao]
                                usersActionAndHist = list(set(filter(lambda x: x in usersAction, usersHist)))

                                bayes = len(usersActionAndHist)/float(len(usersHist))

                                rowResults[acao] = bayes
                        else : 
                            
                            ##### CONTAGEM DE USUÁRIOS QUE FIZERAM TODAS AS AÇÕES DO HISTÓRICO QUE SÃO DIFERENTES DA AÇÃO A SER CALCULADA A PROB
                             
                            #for para inicializar a variavel subset que conterá os usuários
                            firstIndex = len(hist.split('_'))
                            for i in range(len(hist.split('_'))):
                                if hist.split('_')[i] == acao: pass
                                else: 
                                    usersHistNoRepetition = users_action[hist.split('_')[i]]
                                    firstIndex = index
                                    break
                            #outro for para continuar appendando os usuários
                            for index in range(firstIndex, len(hist.split('_'))):
                                if hist.split('_')[index] == acao: pass
                                usersHistNoRepetition = list(set(filter(lambda x: x in users_action[hist.split('_')[index]]  , usersHistNoRepetition)))

                            #### CONTAGEM DE USUÁRIO QUE FIZERAM AÇÃO REPETIDAS VEZES NO HISTÓRICO
                            #lista contendo os usuários que fizeram ação e se repetem na lista totalRepeticoesAcao vezes
                            totalActionRepetitionHist = hist.count(acao)
                            usersHistRepetition = list(set(filter(lambda x: users_action[acao].count(x) == totalActionRepetitionHist, users_action[acao])))

                            #lista contendo os usuários que fizeram ação e se repetem na lista 
                            #totalRepeticoesAcao vezes + 1 que seria a ação a ser calculada a probabilidade
                            totalActionRepetition = totalActionRepetitionHist + 1
                            usersTotalRepetition = list(set(filter(lambda x: users_action[acao].count(x) == totalActionRepetition, users_action[acao])))

                            #lista com todos os usuários que fizeram todas as ações diferentes da ação a ser calculada e
                            #também fizeram a ação calculada X vezes
                            usersHistAndAction = list(set(filter(lambda x: x in  usersTotalRepetition, usersHistNoRepetition)))

                            #lista com todos os usuários que fizeram todas as ações sem repetição do histórico e 
                            #também fizeram a ação repetidas vezes
                            usersHist = list(set(filter(lambda x: x in  usersHistRepetition, usersHistNoRepetition)))

                            bayes = len(usersHistAndAction)/ float(len(usersHist))

                            rowResults[acao] = bayes

                    writer.writerow({'state': hist,'aa': rowResults['aa'], 'ai': rowResults['ai'],'v': rowResults['v'],'ap': rowResults['ap']})

        except:
            import traceback
            traceback.print_exc()
            raise