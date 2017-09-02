# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

	post_id = models.AutoField(primary_key = True)
	post_text = models.TextField()
	post_date = models.DateField(auto_now = True , auto_now_add = False)
	post_time = models.TimeField(auto_now = True , auto_now_add = False)
	post_likes_count = models.IntegerField(default = 0)
	post_comments_count = models.IntegerField(default = 0)
	post_dislikes_count = models.IntegerField(default = 0)
	post_user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.post_text

	