# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count,Sum

from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from postapp.models import Post
from django.template.defaulttags import csrf_token


# Create your views here.  
def userProfile(request):     
	u = request.user     
	if u.is_authenticated:
		t_cnt = Post.objects.filter(post_user = u).count()             
		l_cnt = Post.objects.filter(post_user = u).aggregate(Sum('post_like'))            
		d_cnt = Post.objects.filter(post_user = u).aggregate(Sum('post_dislike')) 
		context = {'name' : u.get_username() , 'fname' : u.get_full_name() , 'total_posts' : t_cnt , 'total_likes' : l_cnt['post_like__sum']
		, 'total_dislikes' : d_cnt['post_dislike__sum']}                     
		return render(request,'userapp/profile.html',context)     
	else:
		return HttpResponse('Please login to see the user profile')


def userLogin(request):
	username = request.POST['uname']
	password = request.POST['psw']
	user = authenticate(request , username = username  , password = password)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect('profile')
	else:
		return render(request,'userapp/login.html')

def home(request):
	return render(request,'userapp/login.html')





