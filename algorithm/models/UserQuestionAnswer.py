# -*- coding: utf-8 -*-
from django.db import models
from .user import User
from .userQuestion import UserQuestion
from .questionOption import QuestionOption

# Resposta do usuário a uma pergunta sobre seu perfil
class UserQuestionAnswer(models.Model):
	user = models.ForeignKey(User)
	user_question = models.ForeignKey(UserQuestion)
	question_option = models.ForeignKey(QuestionOption)
	date = models.DateField(blank=False, auto_created=True, auto_now_add=True)