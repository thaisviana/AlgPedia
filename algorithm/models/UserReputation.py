# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class UserReputation(models.Model):
	reputation = models.FloatField(default=0)
	user = models.ForeignKey(User)
	university = models.ForeignKey(UniversityRank, null=True)
