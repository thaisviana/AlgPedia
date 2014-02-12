# -*- coding: utf-8 -*-
from algorithm.models import Algorithm
from django.core.management.base import BaseCommand
import nltk


class Command(BaseCommand):
    help = u"""Update tags for all algorithms."""

    def handle(self, *args, **options):
        try:
            wnl = nltk.WordNetLemmatizer()
            algorithms = Algorithm.objects.all()
            for alg in algorithms:
                description = alg.description

                # get a list of each word in description.
                tokens = nltk.word_tokenize(description)
                # apply lemmatization. returns the basic form of the words (remove plural, etc)
                # tokens = [wnl.lemmatize(t) for t in tokens]

                pos_tag = nltk.pos_tag(tokens)
                for tag in pos_tag:
                    print tag
                break
        except:
            import traceback
            traceback.print_exc()
            raise
