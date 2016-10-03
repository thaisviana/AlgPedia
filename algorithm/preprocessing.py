# -*- coding: utf-8 -*-
from nltk.stem.lancaster import LancasterStemmer
import nltk
import re
from nltk.corpus import stopwords


def preProcessing(text):
    stemer = LancasterStemmer()
    text = text.lower()
    text = re.sub('\"', '', text)
    text = re.sub('\'', '', text)
    text = re.sub('#', '', text)
    text = re.sub('[^a-zA-Z]+', ' ', text)

    tokens = nltk.word_tokenize(text)
    bagOfWords = {}
    limit_bagOfWords ={}
    for token in tokens:
        if token not in stopwords.words('english') and len(token) > 1:
            token = stemer.stem(token)
            if token in bagOfWords:
                bagOfWords[token] += 1
            else:
                bagOfWords[token] = 1
    return bagOfWords
