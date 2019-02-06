# -*- coding: utf-8 -*-
from django.db import models

# Relacionamento de interesse entre usuario e uma classificacao
class Interest(models.Model):
	classification = models.ForeignKey('Classification', on_delete=models.CASCADE)
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)
