# -*- coding: utf-8 -*-
from django.db import models
from .programmingLanguage import ProgrammingLanguage
from .proeficiencyScale import ProeficiencyScale

class ProgrammingLanguageProeficiencyScale(ProeficiencyScale):
	programming_language = models.ForeignKey(ProgrammingLanguage)