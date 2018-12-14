# -*- coding: utf-8 -*-
from django.db import models
from ..models import classificationProeficiencyScale, ProgrammingLanguageProeficiencyScale
from django.db.models.aggregates import Max

# Resposta de um usuario a uma determinada pergunta sobre uma determinada implementacao
class ImplementationQuestionAnswer(models.Model):
	user = models.ForeignKey('User')
	implementation = models.ForeignKey('Implementation')
	implementation_question = models.ForeignKey('ImplementationQuestion')
	question_option = models.ForeignKey('QuestionOption')
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)
	def save(self, *args, **kwargs):
		super(ImplementationQuestionAnswer, self).save(*args, **kwargs)

	def calculate_user_weight(self):
		PROFILE_WEIGHT = 2
		LANGUAGE_WEIGHT = 3
		KNOWLEDGE_WEIGHT = 5

		classifications_proeficiency = classificationProeficiencyScale.objects.filter(user=self.user).values_list('classification_id', flat=True)
		programminglanguage_proeficiency = ProgrammingLanguageProeficiencyScale.objects.filter(user=self.user).values_list('programming_language_id', flat=True)

		classification_value = 1 if self.implementation.algorithm.classification.id in classifications_proeficiency else 0.5
		language_value = 1 if self.implementation.programming_language.id in programminglanguage_proeficiency else 0.5
		try:
			user_profile_value = self.user.userquestionanswer_set.get(question_option__question_id=1).question_option.value  # user_profile_weight vary from 0 to 10
		except:  # does not exists
			user_profile_value = 1
		user_profile_value /= float(10)

		user_weight = ((PROFILE_WEIGHT * user_profile_value) + (LANGUAGE_WEIGHT * language_value) + (KNOWLEDGE_WEIGHT * classification_value)) \
					  / (PROFILE_WEIGHT + LANGUAGE_WEIGHT + KNOWLEDGE_WEIGHT)
		return user_weight

	def calculate_reputation(self):

		question_weight = self.implementation_question.priority

		max_options_value = float(self.implementation_question.questionoption_set.aggregate(max=Max('value'))['max'])  # answer vary from 0 to questionoption_set max value
		answer = self.question_option.value / max_options_value

		# this value must be (0-1) * [3,4,5]
		reputation = answer * question_weight

		return reputation
