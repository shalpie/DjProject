# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from userapp.models import User
from postapp.models import Post

# Create your models here.

class Comments(models.Model):

	comment_id = models.AutoField('c_id' , primary_key = True)
	comment_text = models.CharField('c_text' , max_length = 200)
	comment_datetime = models.DateTimeField('c_datetime' , auto_now = True , auto_now_add = False)
	comment_user = models.ForeignKey(User , on_delete = models.CASCADE)
	comment_post = models.ForeignKey(Post , on_delete = models.CASCADE)

	def __str__(self):
		return self.comment_text
