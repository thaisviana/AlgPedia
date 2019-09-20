# -*- coding: utf-8 -*-
from django.db import models
from algorithm.models.proeficiencyScale import ProeficiencyScale


class ClassificationProeficiencyScale(ProeficiencyScale):
	classification = models.ForeignKey('Classification', on_delete=models.CASCADE)
