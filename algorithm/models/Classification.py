# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class Classification(models.Model):
	name = models.CharField(max_length=35)
	uri = models.URLField()

	def get_show_url(self):
		return "/show/cat/id/%i" % self.id

	def __str__(self):
		return u'%s' % self.name

	class Meta:
		ordering = ['name']