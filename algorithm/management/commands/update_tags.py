# -*- coding: utf-8 -*-
from algorithm.models import Algorithm, Tag
from algorithm.controllers import *
from django.core.management.base import BaseCommand
from nltk.corpus import stopwords
import nltk
import re
from nltk.stem.lancaster import LancasterStemmer


class Command(BaseCommand):
    help = u"""Update tags for all algorithms."""

    def handle(self, *args, **options):
        try:
            wnl = nltk.WordNetLemmatizer()
            algorithms = Algorithm.objects.all()
            tags = Tag.objects.all()
            f_bayes_var = 0.0
            vecTag = []
            vecBag = []
            sim_matriz = []
            stopwords = ["a", "computational","science","algorithm","program","computer","about", "above", "according", "across", "actually", "after", "again", "against", "all", "almost", "along", "already", "also", "(", ")", ":", ",", "'s", ".", "although", "always", "among", "an", "and", "another", "any", "anything", "are", "aren", "as", "at", "away", "back", "back", "be", "because", "been", "before", "behind", "being", "below", "besides", "better", "between", "beyond", "both", "but", "by", "can", "certain", "could", "do", "does", "during", "each", "else", "enough", "even", "ever", "few", "for", "from", "further", "get", "going", "got", "great", "has", "have", "he", "her", "here", "high", "his", "how", "however", "i", "if", "in", "instead", "into", "is", "it", "its", "itself", "just", "later", "least", "less", "less", "let", "little", "many", "may", "maybe", "me", "might", "more", "most", "much", "must", "neither", "never", "new", "no", "non", "nor", "not", "nothing", "of", "off", "often", "old", "on", "once", "one", "only", "or", "other", "our", "out", "over", "perhaps", "put", "rather", "really", "set", "several", "she", "should", "since", "snot", "snt", "so", "some", "something", "sometimes", "soon", "still", "such", "t", "than", "that", "the", "their", "them", "then", "there", "therefore", "these", "they", "thing", "this", "those", "though", "three", "through", "till", "to", "together", "too", "toward", "towards", "two", "under", "up", "upon", "us", "very", "very", "was", "were", "what", "when", "where", "whether", "which", "while", "whole", "whose", "will", "with", "within", "without", "would", "yet", "you", "your"]
            
            stemer = LancasterStemmer()
            
            i =0
            
            for alg in algorithms:
                description_alg = alg.description
                description_alg = description_alg.lower()
                description_alg = re.sub('[^a-z]', ' ', description_alg)
                            
                tokens = nltk.word_tokenize(description_alg)
                bagOfWords = {} 
                for token in tokens:
                    if token not in stopwords:
                        token = stemer.stem(token)
                        
                        if token in bagOfWords:
                            bagOfWords[token] += 1
                        else:
                            bagOfWords[token] = 1
                            
                vecBag += [bagOfWords]
                vecTag.append( alg.tags.all())
            
            
            for i in range(0, len(algorithms)):
                linha = []
                for j in range(0, len(algorithms)):
                    linha += [ cosine_similarity(vecBag[i], vecBag[j]) ]
                sim_matriz += [linha]
                 
            
            for tag in tags:
                for alg in algorithms:
                    if ( f_bayes(tag, alg.id-1, sim_matriz, vecTag) > 0.2 ):
                        if tag not in vecTag[alg.id-1]:
                            #print alg.id, " ==> " , tag.name
                            alg.tags.add(tag)
                            alg.save()
                             
        except:
            import traceback
            traceback.print_exc()
            raise
