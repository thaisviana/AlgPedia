# -*- coding: utf-8 -*-
from django.db import models
from .classification import Classification
from .proeficiencyScale import ProeficiencyScale

class ClassificationProeficiencyScale(ProeficiencyScale):
	classification = models.ForeignKey(Classification)