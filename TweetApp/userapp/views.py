# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count,Sum
from .models import User
from postapp.models import Post


# Create your views here. 
def displayUser(request):
	u = User.objects.get(pk = 2)
	t_cnt = Post.objects.filter(post_user__user_id = u.user_id).count()
	l_cnt = Post.objects.filter(post_user__user_id = u.user_id).aggregate(Sum('post_like')) 
	d_cnt = Post.objects.filter(post_user__user_id = u.user_id).aggregate(Sum('post_dislike'))     
	str = 'Welcome %s Age %s email %s total post %d total likes %s total dislike %s' % (u.user_name
	,u.user_dob,u.user_email,t_cnt,l_cnt['post_like__sum'],d_cnt['post_dislike__sum'])     
	return HttpResponse(str)

