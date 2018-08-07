# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class AlgorithmFullText(models.Model):
	alg_name = models.CharField(max_length=30)
	description = models.TextField()
