# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

# Questao de escala em relacao a algo
class Question(models.Model):
	text = models.TextField()
	priority = models.IntegerField()