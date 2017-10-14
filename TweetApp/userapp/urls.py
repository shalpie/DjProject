"""TweetApp URL Configuration"""

from django.conf.urls import url , include
from django.contrib import admin
from .views import UserProfile
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'userapp'

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name = 'userapp/login.html') , name = 'home'),
	url(r'^login$', auth_views.login , {'template_name': 'userapp/login.html'} , name = 'userLogin'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'} , name='userLogout'),
    url(r'^userapp/profile$', UserProfile.as_view() , name = 'userProfile'),
    
    
]
