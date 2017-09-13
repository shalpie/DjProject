# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase , Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import SESSION_KEY
from commentapp.models import Comment
from postapp.models import Post

# Create your tests here.
class CommentTest(TestCase):

	def setUp(self):
		self.client = Client()

		self.test_user_1 = User.objects.create_user(username = 'test_user_1' , password = 'test_user_1')
		self.test_user_2  = User.objects.create_user(username = 'test_user_2' , password = 'test_user_2')
		self.test_user_3  = User.objects.create_user(username = 'test_user_3' , password = 'test_user_3')

		self.test_user_1_post = Post.objects.create(post_text  = 'Hows the testing going' , post_user = self.test_user_1)

		self.comment_1_by_user_1 = Comment.objects.create(comment_text = 'Hurray tested' , comment_user = self.test_user_1 , comment_post = self.test_user_1_post ) 
		self.comment_2_by_user_1 = Comment.objects.create(comment_text = 'Hurray done ' , comment_user = self.test_user_1 , comment_post = self.test_user_1_post) 
		self.comment_2_by_user_2 = Comment.objects.create(comment_text = 'Not expected ' , comment_user = self.test_user_2 , comment_post = self.test_user_1_post) 
	

	
	def test_comment_display_when_no_comments_available(self):
		self.client.login(username = 'test_user_3' , password = 'test_user_3')
		response = self.client.post(reverse('commentapp:postComment'))
		self.assertContains(response,'No comments are available')
		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.context['comment_list'].exists())


	def test_comment_display_when_comments_available(self):
		self.client.login(username = 'test_user_1' , password = 'test_user_1')
		response = self.client.post(reverse('commentapp:postComment'))
		self.assertEqual(response.status_code, 200)
		self.assertNotContains(response,'No comments are available')
		self.assertTrue(response.context['comment_list'].exists())
		self.assertEqual(response.context['comment_list'].count(),2)


		

