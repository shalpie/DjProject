# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase , Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import SESSION_KEY

# Create your tests here.
class UserTest(TestCase):

	

	def setUp(self):
		self.client = Client()
		self.user  = User.objects.create_user(username = 'test' , password = 'test')
		self.client.login(username = 'test' , password = 'test')


	def test_defualt_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
		
	def test_login_function(self):
		
		response = self.client.post(reverse('userapp:userProfile'))
		self.assertContains(response,'Welcome test')
		self.assertEqual(response.status_code,200)

	def test_logout_function(self):
		self.assertTrue(SESSION_KEY in self.client.session)
		response = self.client.post(reverse('userapp:userLogout'), follow = True)
		self.assertEqual(response.status_code,200)
		#print self.client.session.keys()
		self.assertFalse(SESSION_KEY in self.client.session)
		#print response.context['request'].user.is_authenticated()


		
	
