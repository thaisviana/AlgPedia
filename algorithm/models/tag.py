# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def register_admin(cls):
         admin.site.register(cls, Admin)

    class Meta:
        abstract = False


class Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
