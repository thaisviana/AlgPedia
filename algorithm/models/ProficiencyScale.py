# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

# Classe base de proeficiencia do usuario em algo
class ProeficiencyScale(models.Model):
	user = models.ForeignKey(User)
	value = models.IntegerField()