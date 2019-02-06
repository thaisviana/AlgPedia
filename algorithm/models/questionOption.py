# -*- coding: utf-8 -*-
from django.db import models

# Respostas validas para as perguntas
class QuestionOption(models.Model):
	question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questionoption_set')
	value = models.IntegerField()
	text = models.TextField()
