# -*- coding: utf-8 -*-
from django.db import models

# Questao de escala em relacao a algo
class Question(models.Model):
	text = models.TextField()
	priority = models.IntegerField()