from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from . import views

app_name = 'mysite_app'
urlpatterns = [
	url(r'^$', views.home, name='home'),
]
