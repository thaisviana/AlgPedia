# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class ProgrammingLanguage(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return u'%s' % self.name
