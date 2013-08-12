from django.db import models
from django.contrib.auth.models import User

class ProgrammingLanguage(models.Model):
	name = models.CharField(max_length=10)
	
	def __unicode__(self):
		return u'%s' % self.name

class Classification(models.Model):
	name = models.CharField(max_length=35)
	uri = models.URLField()
	
	def get_show_url(self):
		return "http://localhost:8000/show/cat/id/%i" % self.id 
	
	def __unicode__(self):
		return u'%s' % self.name
		
class Algorithm(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	classification = models.ForeignKey(Classification, null=True, blank=True)
	uri = models.URLField()
	visible = models.BooleanField()
	reputation = models.FloatField()
	
	def get_show_url(self):
		return "http://localhost:8000/show/alg/id/%i" % self.id
	
	def __unicode__(self):
		return u'%s' % self.name.lower().title()

class Implementation(models.Model):
	# an algorithm can have many implementations
	algorithm = models.ForeignKey(Algorithm)
	code = models.TextField()
	programming_language = models.ForeignKey(ProgrammingLanguage)
	visible = models.BooleanField()
	reputation = models.FloatField()
	
	def __unicode__(self):
		return u'%s' % self.code
	
	def get_show_url(self):
		return "http://localhost:8000/show/imp/id/%i" % self.id

###################

# Relacionamento de interesse entre usuario e uma classificacao
class Interest(models.Model):
	classification = models.ForeignKey(Classification)
	user = models.ForeignKey(User)

#Classe base de proeficiencia do usuario em algo
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
class QuestionAnswer(models.Model):
	question = models.ForeignKey(Question)
	value = models.IntegerField()
	text = models.TextField()

# Pergunta em relacao ao usuario
class UserQuestion(Question):
	pass
	
class UserQuestionAnswer(models.Model):
	user = models.ForeignKey(User)
	user_question = models.ForeignKey(UserQuestion)
	question_answer = models.ForeignKey(QuestionAnswer)
	
# Pergunta em relacao a uma implementacao
class ImplementationQuestion(Question):
	pass

# Resposta de um usuario a uma determinada pergunta sobre uma determinada implementacao
class ImplementationQuestionAnswer(models.Model):
	user = models.ForeignKey(User)
	implementation = models.ForeignKey(Implementation)
	implementation_question = models.ForeignKey(ImplementationQuestion)
	question_answer = models.ForeignKey(QuestionAnswer)
