# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
SEX = (('M','Male'),('F','Female'))

class User(models.Model):

	user_id = models.AutoField('u_id' , primary_key = True)
	user_name = models.CharField('u_name', max_length = 100)
	user_password = models.CharField('u_pwd', max_length = 100)
	user_sex = models.CharField('u_sex' , max_length = 6 , choices = SEX)
	user_email = models.EmailField('u_email' , max_length = 50)
	user_dob = models.DateField('u_dob' , auto_now = False , auto_now_add = False)
	user_joindate = models.DateTimeField('u_join_date' , auto_now = False , auto_now_add = True)

	def __str__(self):
		return self.user_name


