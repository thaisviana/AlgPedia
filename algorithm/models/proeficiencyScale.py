# -*- coding: utf-8 -*-
from django.db import models
from .user import User

# Classe base de proeficiencia do usuario em algo
class ProeficiencyScale(models.Model):
	user = models.ForeignKey(User)
	value = models.IntegerField()