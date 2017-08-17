# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Post
from django.contrib.auth.models import User
from commentapp.models import Comment

# Create your views here.
def showTweet(request):
	""" The default view to display the user tweets"""
	print 'came show'
	u = request.user
	if u.is_authenticated:
		post_list = Post.objects.filter(post_user = u)
		context = { 'user' : u , 'post_list' : post_list}
		return render(request,'postapp/index.html',context)
	else:
		return HttpResponse('Please login to post anything')


def detailTweet(request, post_id):
	""" Display the tweets's details """
	post = Post.objects.get(post_id = post_id)
	comments = Comment.objects.filter(comment_post__post_id = post_id)
	context = { 'post' : post , 'comments' : comments}
	return render(request,'postapp/detail.html',context)
	
def postTweet(request):
	""" Post the user tweet"""
	print 'came'
	u = request.user
	if u.is_authenticated:
		text = request.POST['text']
		if text:	
			post = Post(post_text = text , post_user = u)
			post.save()
			return HttpResponseRedirect('/post')
	#		post_list = Post.objects.filter(post_user = u)
	#		context = { 'user' : u , 'post_list' : post_list}
	#		return render(request,'postapp/index.html')

	else:
		return HttpResponse('Please login to post anything')