# -*- coding: utf-8 -*-
from django.db import models


# Classe base de proeficiencia do usuario em algo
class ProeficiencyScale(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	value = models.IntegerField()
