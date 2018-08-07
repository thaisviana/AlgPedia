# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class Algorithm(models.Model):
	name = models.CharField(max_length=80)
	description = models.TextField()
	classification = models.ForeignKey(Classification, null=True, blank=True)
	uri = models.URLField()
	visible = models.BooleanField()
	reputation = models.FloatField(default=0)
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)

	tags = models.ManyToManyField(Tag, blank=True, null=True)

	user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"Creator")

	def get_show_url(self):
		return "/show/alg/id/%i" % self.id

	def __str__(self):
		return u'%s' % self.name.lower().title()

	def calculate_reputation(self):
		reputation = self.implementation_set.aggregate(average=Avg('reputation'))['average'] or None
		self.reputation = reputation
		self.save()
