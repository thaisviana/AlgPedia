# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

# Relacionamento de interesse entre usuario e uma classificacao
class Interest(models.Model):
	classification = models.ForeignKey(Classification)
	user = models.ForeignKey(User)
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)