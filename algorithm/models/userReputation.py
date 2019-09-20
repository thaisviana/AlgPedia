# -*- coding: utf-8 -*-
from django.db import models

class UserReputation(models.Model):
	reputation = models.FloatField(default=0)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	university = models.ForeignKey('UniversityRank', on_delete=models.CASCADE, null=True)
