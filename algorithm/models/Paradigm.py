# -*- coding: utf-8 -*-
from django.db import models

class Paradigm(models.Model):
	##["paradigm", "wpage", "abstract", "label"]
	dbpedia_uri = models.CharField(max_length=100)
	wikipedia_uri = models.CharField(max_length=100)
	label = models.CharField(max_length=100)
	abstract = models.TextField()

	def get_show_url(self):
		return "/show/para/id/%i" % self.id

	def __str__(self):
		return u'%s' % self.label
