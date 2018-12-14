# -*- coding: utf-8 -*-
from algorithm.models import algorithm, tag , classification, ProgrammingLanguage, Implementation
from django.core.management.base import BaseCommand
import sys

class Command(BaseCommand):
    help = u"""generate owl."""

    def handle(self, *args, **options):
		reload(sys)
		sys.setdefaultencoding("utf-8")
		algorithms = algorithm.objects.all()
		a = open("owl.txt", 'w')
		
		#DECLARA ALGORITMOS
		a.write("<Declaration> \n")
		a.write('''<Class IRI="#ALGORITHM"/> \n''')
		a.write("</Declaration> \n")
		
		#DECLARA CLASSIFICACOES
		a.write("<Declaration> \n")
		a.write('''<Class IRI="#CLASSIFICATION"/> \n''')
		a.write("</Declaration> \n")
		
		#DECLARA CLASSIFICACOES
		a.write("<Declaration> \n")
		a.write('''<Class IRI="#PROGRAMMING_LANGUAGE"/> \n''')
		a.write("</Declaration> \n")
		
		#DECLARA INDIVIDUOS DE ALGORITMOS
		algorithms = algorithm.objects.all()
		for algorithm in algorithms :
			a.write("<Declaration> \n")
			a.write('''<NamedIndividual IRI="#'''+algorithm.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</Declaration> \n")
		
		
		#DECLARA INDIVIDUOS DE CLASSIFICACOES
		for classification in classification.objects.all():
			a.write("<Declaration> \n")
			a.write('''<NamedIndividual IRI="#'''+classification.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</Declaration> \n")
		
		#DECLARA INDIVIDUOS DE PROGRAMMING_LANGUAGE
		for pl in ProgrammingLanguage.objects.all():
			a.write("<Declaration> \n")
			a.write('''<NamedIndividual IRI="#'''+pl.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</Declaration> \n")
		
		#DECLARA INDIVIDUOS DE ALGORITMOS PERTENCEM A CLASSE ALGORITMOS
		for algorithm in algorithms :
			a.write("<ClassAssertion> \n")
			a.write('''<Class IRI="#ALGORITHM"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+algorithm.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</ClassAssertion> \n")
			
		#DECLARA INDIVIDUOS DE CLASSIFICACOES PERTENCEM A CLASSE CLASSIFICACOES
		for classification in classification.objects.all():
			a.write("<ClassAssertion> \n")
			a.write('''<Class IRI="#CLASSIFICATION"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+classification.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</ClassAssertion> \n")
			
		#DECLARA INDIVIDUOS DE PROGRAMMING_LANGUAGE  PERTENCEM A CLASSE PROGRAMMING_LANGUAGE
		for pl in ProgrammingLanguage.objects.all():
			a.write("<ClassAssertion> \n")
			a.write('''<Class IRI="#PROGRAMMING_LANGUAGE"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+pl.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</ClassAssertion> \n")
			
		for algorithm in algorithms :
			a.write("<ObjectPropertyAssertion> \n")
			a.write('''<ObjectProperty IRI="#belongs"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+algorithm.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+algorithm.classification.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</ObjectPropertyAssertion> \n")
		
		
		for i in Implementation.objects.all():
			a.write("<ObjectPropertyAssertion> \n")
			a.write('''<ObjectProperty IRI="#implementation"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+i.algorithm.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write('''<NamedIndividual IRI="#'''+i.programming_language.name.strip().replace(" ", "_")+'''"/> \n''')
			a.write("</ObjectPropertyAssertion> \n")
			

		a.close()
		