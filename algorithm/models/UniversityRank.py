# -*- coding: utf-8 -*-
from django.db import models

class UniversityRank(models.Model):
	name = models.CharField(max_length=60)
	position = models.IntegerField()

	class Meta:
		ordering = ['position']