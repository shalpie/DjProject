# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.dispatch import receiver

from postapp.models import Post
from commentapp.models import Comment
from postapp.signals import new_post

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
		new_post.connect(send_notification_mail)
		new_post.send(sender=Post, sig_post=post)
		return HttpResponseRedirect('/post')

@receiver(new_post)
def send_notification_mail(sender, sig_post, **kwargs):
	"""  Send mail as User posts something """
	str1 =  str(sig_post.post_text) + str(sig_post.post_user)
	user = User.objects.get(username = str(sig_post.post_user))
	subject = 'new post'
	message = str(sig_post.post_text) 
	sender =  'shalgitunix@gmail.com'
	recepient_list = []
	recepient_list.append(str(user.email)) 
	send_mail(subject, message, sender, recepient_list)

			
		
	