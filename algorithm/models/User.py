# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class User(AbstractUser):
	class Meta:
		verbose_name = "user"
		verbose_name_plural = "users"

	def is_moderator(self):
		count = self.groups.filter(name='Moderator').count()
		if count:
			return True
		else:
			return False

	def programming_languages(self):
		return ProgrammingLanguageProeficiencyScale.objects.filter(user=self).only("programming_language")
