# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

# Respostas validas para as perguntas
class QuestionOption(models.Model):
	question = models.ForeignKey(Question, related_name='questionoption_set')
	value = models.IntegerField()
	text = models.TextField()