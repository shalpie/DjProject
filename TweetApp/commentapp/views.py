# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Comments
from userapp.models import User

# Create your views here.
def postComment(request):
	u = User.objects.get(pk = 1)
	comments = Comments.objects.filter(comment_user__user_id = u.user_id)
	t = ' || '.join(c.comment_text for c in comments)
	str = 'Comments: ' + t + ' by ' + u.user_name
	return HttpResponse(str)