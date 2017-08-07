# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

	post_id = models.AutoField('p_id', primary_key = True)
	post_text = models.TextField('p_text')
	post_date = models.DateField('p_date', auto_now = True , auto_now_add = False)
	post_time = models.TimeField('p_time', auto_now = True , auto_now_add = False)
	post_like = models.IntegerField('p_like', default = 0)
	post_comments = models.IntegerField('p_comm', default = 0)
	post_dislike = models.IntegerField('p_dislike', default = 0)
	post_user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.post_text