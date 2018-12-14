# -*- coding: utf-8 -*-
from django.db import models

class AlgorithmFullText(models.Model):
	alg_name = models.CharField(max_length=30)
	description = models.TextField()
