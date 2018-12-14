# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class UniversityRank(models.Model):
	name = models.CharField(max_length=60)
	position = models.IntegerField()

	@classmethod
	def register_admin(cls):
		admin.site.register(cls, Admin)

	class Meta:
		abstract = False
		ordering = ['position',]


class Admin(admin.ModelAdmin):
	list_display = ('name', 'position', )
	search_fields = ('name', )