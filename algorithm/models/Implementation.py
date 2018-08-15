# -*- coding: utf-8 -*-
from django.db import models
from .programmingLanguage import ProgrammingLanguage
from .algorithm import Algorithm
from .user import User

class Implementation(models.Model):
	# an algorithm can have many implementations
	algorithm = models.ForeignKey(Algorithm, related_name='implementation_set')
	code = models.TextField()
	programming_language = models.ForeignKey(ProgrammingLanguage)
	visible = models.BooleanField()
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)
	reputation = models.FloatField(default=0)
	accumulated_weight = models.FloatField(default=0)
	user = models.ForeignKey(User, null=True, blank=True, verbose_name=u"Creator")

	def __str__(self):
		return u'%s' % self.code

	def get_show_url(self):
		return "/show/imp/id/%i" % self.id

	def save_reputation(self, reputation, user_weight):
		if not self.reputation:
			self.reputation = 0
		# Média ponderada pelos pesos dos usuários de todas as reputações daquela implementação.
		self.reputation = ((self.reputation * self.accumulated_weight) + reputation * user_weight) / float(self.accumulated_weight + user_weight)
		self.accumulated_weight = self.accumulated_weight + user_weight
		self.save()
		return True