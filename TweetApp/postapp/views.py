# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from commentapp.models import Comment
from django.contrib.auth.decorators import login_required
from postapp.models import Post


# Create your views here.
@login_required
def showTweet(request):
	""" The default view to display the user tweets"""
	u = request.user
	user_post_list = Post.objects.filter(post_user = u)
	friends_post_list = Post.objects.exclude(post_user = u)
	context = { 'user' : u , 'user_post_list' : user_post_list  , 'friends_post_list' : friends_post_list}
	return render(request,'postapp/index.html',context)
		
	

@login_required
def detailTweet(request, post_id):
	""" Display the tweets's details """
	post = Post.objects.get(post_id = post_id)
	comments = Comment.objects.filter(comment_post__post_id = post_id)
	context = { 'post' : post , 'comments' : comments}
	return render(request,'postapp/detail.html',context)
	
@login_required
def postTweet(request):
	""" Post the user tweet"""
	u = request.user
	text = request.POST['text']
	if text:
		post = Post(post_text = text , post_user = u)
		post.save()
	#	post_saved.send(sender=Post, sig_post=post, sig_user=u)
		return HttpResponseRedirect('/post')
			
		
	