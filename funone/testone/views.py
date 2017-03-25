from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'testone/index.html'

	def get_queryset(self):
		pass