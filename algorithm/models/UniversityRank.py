# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class UniversityRank(models.Model):
	name = models.CharField(max_length=60)
	position = models.IntegerField()

	class Meta:
		ordering = ['position']