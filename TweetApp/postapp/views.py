# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.dispatch import receiver
import logging

from postapp.models import Post
from commentapp.models import Comment
from postapp.signals import new_post

dblog = logging.getLogger(__name__)

@method_decorator(login_required, name = 'dispatch')
class TweetList(ListView):

	""" Display the user and friends' tweets"""

	model = Post
	template_name = 'postapp/index.html'
	
	def get_context_data(self):
		u = self.request.user
		dblog.info('showTweet')
		context = super(TweetList,self).get_context_data()
		user_post_list = Post.objects.filter(post_user = u)
		friends_post_list = Post.objects.exclude(post_user = u)
		context = { 'user' : u , 'user_post_list' : user_post_list  , 'friends_post_list' : friends_post_list}
		return context

@method_decorator(login_required, name = 'dispatch')
class TweetDetail(DetailView):

	""" Display the tweets' details"""
	model = Post
	template_name = 'postapp/detail.html'
	pk_url_kwarg = 'post_id'
	
	def get_context_data(self, **kwargs):
		dblog.info('detailTweet ')
		id = kwargs['object'].post_id
		context = super(TweetDetail,self).get_context_data(**kwargs)
		post = Post.objects.get(post_id = id)
		comments = Comment.objects.filter(comment_post__post_id = id)
		context = { 'post' : post , 'comments' : comments}
		return context

@method_decorator(login_required, name = 'dispatch')
class TweetPost(RedirectView):

	"""  Send mail as User posts something """

	pattern_name = 'postapp:showTweet'

	def get_redirect_url(self, *args, **kwargs):
		dblog.info('postTweet')
		u = self.request.user
		text = self.request.POST['text']
		if text:
			post = Post(post_text = text , post_user = u)
			post.save()
			new_post.connect(self.send_notification_mail)
			new_post.send(sender=Post, sig_post=post)
			url = super(TweetPost, self).get_redirect_url(*args, **kwargs) 
			return url

	@method_decorator(receiver(new_post) , name = 'dispatch')
	def send_notification_mail(self, sender, sig_post, **kwargs):
			
		dblog.info('notification receiver')
		str1 =  str(sig_post.post_text) + str(sig_post.post_user)
		user = User.objects.get(username = str(sig_post.post_user))
		subject = 'new post'
		message = str(sig_post.post_text) 
		sender =  'shalgitunix@gmail.com'
		recepient_list = []
		recepient_list.append(str(user.email)) 
		send_mail(subject, message, sender, recepient_list)




			
		
	