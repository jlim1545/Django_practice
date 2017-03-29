from django.conf.urls import url

from . import views

app_name = 'airplane'

urlpatterns = [
	url(r'^$', views.index, name='index'),
]