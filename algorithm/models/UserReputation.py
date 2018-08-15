# -*- coding: utf-8 -*-
from django.db import models
from .user import User
from .universityRank import UniversityRank

class UserReputation(models.Model):
	reputation = models.FloatField(default=0)
	user = models.ForeignKey(User)
	university = models.ForeignKey(UniversityRank, null=True)
