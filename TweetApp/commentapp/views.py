# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.views.generic import ListView
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Comment

# Create your views here.

dblog = logging.getLogger(__name__)

@method_decorator(login_required, name = 'dispatch')
class ListCommentByUser(ListView):

	""" View the list of user comments"""

	template_name = 'commentapp/index.html'
	context_object_name = 'comment_list'


	def get_queryset(self):
		return Comment.objects.filter(comment_user  = self.request.user)


# @login_required
# def postComment(request):
# 	""" View the user comments"""
# 	u = request.user
# 	comment_list = Comment.objects.filter(comment_user  = u)
# 	dblog.info('postComment')
# 	context = { 'user' : u , 'comment_list' : comment_list}
# 	return render(request,'commentapp/index.html',context)
		
	
	