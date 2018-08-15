# -*- coding: utf-8 -*-
from django.db import models
from .question import Question

# Respostas validas para as perguntas
class QuestionOption(models.Model):
	question = models.ForeignKey(Question, related_name='questionoption_set')
	value = models.IntegerField()
	text = models.TextField()