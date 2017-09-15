# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

dblog = logging.getLogger(__name__)

@login_required
def postComment(request):
	""" View the user comments"""
	u = request.user
	comment_list = Comment.objects.filter(comment_user  = u)
	dblog.info('postComment')
	context = { 'user' : u , 'comment_list' : comment_list}
	return render(request,'commentapp/index.html',context)
		
	
	