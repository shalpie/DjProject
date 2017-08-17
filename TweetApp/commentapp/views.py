# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def postComment(request):
	u = request.user
	if u.is_authenticated:
		comment_list = Comment.objects.filter(comment_user  = u)
		context = { 'user' : u , 'comment_list' : comment_list}
		return render(request,'commentapp/index.html',context)
	else:
		return HttpResponse('Please login to see the user profile')
	