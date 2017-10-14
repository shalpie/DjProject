# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.db.models import Count,Sum
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from postapp.models import Post


dblog = logging.getLogger(__name__)

@method_decorator(login_required , name = 'dispatch')
class UserProfile(TemplateView):

	template_name = 'userapp/profile.html'		
#	context_object_name = 'user_profile_details'

	def get_context_data(self):
		context = super(UserProfile,self).get_context_data()

		u = self.request.user   
		dblog.info('userProfile')  
		likes = Post.objects.filter(post_user = u).aggregate(Sum('post_likes_count'))
		dislikes = Post.objects.filter(post_user = u).aggregate(Sum('post_dislikes_count'))
		context['name'] = u.get_username()
		context['fullname'] = u.get_full_name()
		context['total_user_posts'] = Post.objects.filter(post_user = u).count()
		context['total_user_likes'] = likes['post_likes_count__sum']
		context['total_user_dislikes'] = dislikes['post_dislikes_count__sum']
		return context
	




