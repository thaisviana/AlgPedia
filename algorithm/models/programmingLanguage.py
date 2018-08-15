# -*- coding: utf-8 -*-
from django.db import models

class ProgrammingLanguage(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return u'%s' % self.name
