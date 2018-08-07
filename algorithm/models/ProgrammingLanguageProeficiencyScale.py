# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Avg, Max

class ProgrammingLanguageProeficiencyScale(ProeficiencyScale):
	programming_language = models.ForeignKey(ProgrammingLanguage)