# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.aggregates import Avg, Max


class CustomUser(User):
	class Meta:
		proxy = True
	def is_moderator(self):
		count = self.groups.filter(name='Moderator').count()
		if count:
			return True
		else:
			return False

	def programming_languages(self):
		return ProgrammingLanguageProeficiencyScale.objects.filter(user=self).only("programming_language")

class ProgrammingLanguage(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return u'%s' % self.name

class Classification(models.Model):
	name = models.CharField(max_length=35)
	uri = models.URLField()

	def get_show_url(self):
		return "/show/cat/id/%i" % self.id

	def __unicode__(self):
		return u'%s' % self.name

	class Meta:
		ordering = ['name']


class Algorithm(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	classification = models.ForeignKey(Classification, null=True, blank=True)
	uri = models.URLField()
	visible = models.BooleanField()
	reputation = models.FloatField(default=0)

	user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"Creator")

	def get_show_url(self):
		return "/show/alg/id/%i" % self.id

	def __unicode__(self):
		return u'%s' % self.name.lower().title()

	def calculate_reputation(self):
		reputation = self.implementation_set.aggregate(average=Avg('reputation'))['average'] or None
		self.reputation = reputation
		self.save()


class Implementation(models.Model):
	# an algorithm can have many implementations
	algorithm = models.ForeignKey(Algorithm, related_name='implementation_set')
	code = models.TextField()
	programming_language = models.ForeignKey(ProgrammingLanguage)
	visible = models.BooleanField()

	reputation = models.FloatField(default=0)
	evaluation_count = models.IntegerField(default=0)

	user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"Creator")

	def __unicode__(self):
		return u'%s' % self.code

	def get_show_url(self):
		return "/show/imp/id/%i" % self.id

	def save_reputation(self, reputation, user_weight):
		# change evaluation_count to accumulated weight
		self.reputation = ((self.reputation * self.evaluation_count) + reputation * user_weight) / float(self.evaluation_count + user_weight)
		self.evaluation_count = self.evaluation_count + user_weight
		self.save()
		return True

###################

# Relacionamento de interesse entre usuario e uma classificacao
class Interest(models.Model):
	classification = models.ForeignKey(Classification)
	user = models.ForeignKey(User)

# Classe base de proeficiencia do usuario em algo
class ProeficiencyScale(models.Model):
	user = models.ForeignKey(User)
	value = models.IntegerField()

class ProgrammingLanguageProeficiencyScale(ProeficiencyScale):
	programming_language = models.ForeignKey(ProgrammingLanguage)

class ClassificationProeficiencyScale(ProeficiencyScale):
	classification = models.ForeignKey(Classification)

# Questao de escala em relacao a algo
class Question(models.Model):
	text = models.TextField()
	priority = models.IntegerField()

# Respostas validas para as perguntas
class QuestionOption(models.Model):
	question = models.ForeignKey(Question, related_name='questionoption_set')
	value = models.IntegerField()
	text = models.TextField()

# Pergunta em relacao ao usuario
class UserQuestion(Question):
	pass

# Resposta do usuário a uma pergunta sobre seu perfil
class UserQuestionAnswer(models.Model):
	user = models.ForeignKey(User)
	user_question = models.ForeignKey(UserQuestion)
	question_option = models.ForeignKey(QuestionOption)

# Pergunta em relacao a uma implementacao
class ImplementationQuestion(Question):
	pass


# Resposta de um usuario a uma determinada pergunta sobre uma determinada implementacao
class ImplementationQuestionAnswer(models.Model):
	user = models.ForeignKey(User)
	implementation = models.ForeignKey(Implementation)
	implementation_question = models.ForeignKey(ImplementationQuestion)
	question_option = models.ForeignKey(QuestionOption)

	def save(self, *args, **kwargs):
		super(ImplementationQuestionAnswer, self).save(*args, **kwargs)

	def calculate_user_weight(self):
		classifications_proeficiency = ClassificationProeficiencyScale.objects.filter(user=self.user).values_list('classification_id', flat=True)
		programminglanguage_proeficiency = ProgrammingLanguageProeficiencyScale.objects.filter(user=self.user).values_list('programming_language_id', flat=True)

		classification_weight = 1 if self.implementation.algorithm.classification.id in classifications_proeficiency else 0.5
		language_weight = 1 if self.implementation.programming_language.id in programminglanguage_proeficiency else 0.5
		try:
			user_profile_weight = self.user.userquestionanswer_set.get(question_option__question_id=1).question_option.value / float(10)  # user_profile_weight vary from 0 to 10
		except:  # does not exists
			user_profile_weight = 0.1
		user_weight = user_profile_weight * language_weight * classification_weight
		return user_weight

	def calculate_reputation(self):

		question_weight = self.implementation_question.priority

		max_options_value = float(self.implementation_question.questionoption_set.aggregate(max=Max('value'))['max'])  # answer vary from 0 to questionoption_set max value
		answer = self.question_option.value / max_options_value

		# this value must be (0-1) * [3,4,5]
		reputation = answer * question_weight

		return reputation
