from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.views import generic
from django.shortcuts import render

# # Create your views here.
# class IndexView(generic):
# 	template_name = 'testone/base.html'

# 	def get_queryset(self):
# 		pass

def index(request):
	return render(request, "testone/index.html", {})

def home_files(reqeuest, filename):
	return render(request, filename, {}, content_type="text/plain")