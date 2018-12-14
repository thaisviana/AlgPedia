# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Classification(models.Model):
	name = models.CharField(max_length=35)
	uri = models.URLField()

	def get_show_url(self):
		return "/show/cat/id/%i" % self.id

	def __str__(self):
		return u'%s' % self.name

	@classmethod
	def register_admin(cls):
		admin.site.register(cls, Admin)

	class Meta:
		ordering = ['name']

class Admin(admin.ModelAdmin):
	list_display = ('name', 'uri',)
	search_fields = ('name',)