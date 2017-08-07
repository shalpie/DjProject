# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from commentapp.models import Comment

# Create your views here.
def postTweet(request):
	u = request.user
	if u.is_authenticated:
		post_list = Post.objects.filter(post_user = u)
		context = { 'user' : u , 'post_list' : post_list}
		return render(request,'postapp/index.html',context)
	else:
		return HttpResponse('Please login to post anything')


def detailTweet(request, post_id):
	post = Post.objects.get(post_id = post_id)
	comments = Comment.objects.filter(comment_post__post_id = post_id)
	context = { 'post' : post , 'comments' : comments}
	return render(request,'postapp/detail.html',context)
	