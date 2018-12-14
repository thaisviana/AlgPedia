# -*- coding: utf-8 -*-
from django.db import models
from ..models.proeficiencyScale import ProeficiencyScale


class ProgrammingLanguageProeficiencyScale(ProeficiencyScale):
	programming_language = models.ForeignKey('ProgrammingLanguage')
