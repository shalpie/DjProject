# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count,Sum
import logging

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from postapp.models import Post
from django.template.defaulttags import csrf_token
from django.contrib.auth.decorators import login_required

dblog = logging.getLogger(__name__)

# Create your views here.
@login_required  
def userProfile(request):
	""" View the user profile"""     
	u = request.user     
	user_posts_count = Post.objects.filter(post_user = u).count()             
	user_likes_count = Post.objects.filter(post_user = u).aggregate(Sum('post_likes_count'))            
	user_dislikes_count = Post.objects.filter(post_user = u).aggregate(Sum('post_dislikes_count')) 
	dblog.info('userProfile')
	context = {'name' : u.get_username() , 'fullname' : u.get_full_name() , 'total_user_posts' :user_posts_count , 'total_user_likes' : user_likes_count['post_likes_count__sum']
	, 'total_user_dislikes' : user_dislikes_count['post_dislikes_count__sum']}                     
	return render(request,'userapp/profile.html',context)
		     
	
def home(request):
	""" home page redirection""" 
	return render(request,'userapp/login.html')
	




