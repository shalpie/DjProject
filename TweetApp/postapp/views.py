# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from userapp.models import User

# Create your views here.
def postTweet(request):
	u = User.objects.get(pk = 1)
	posts = Post.objects.filter(post_user__user_id = u.user_id)
	str = ' || '.join(p.post_text for p in posts)
	str = 'Comments : ' + str + ' by ' + u.user_name
	return HttpResponse(str)