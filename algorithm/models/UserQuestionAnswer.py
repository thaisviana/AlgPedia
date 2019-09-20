# -*- coding: utf-8 -*-
from django.db import models

# Resposta do usuário a uma pergunta sobre seu perfil
class UserQuestionAnswer(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	user_question = models.ForeignKey('UserQuestion', on_delete=models.CASCADE)
	question_option = models.ForeignKey('QuestionOption', on_delete=models.CASCADE)
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)
