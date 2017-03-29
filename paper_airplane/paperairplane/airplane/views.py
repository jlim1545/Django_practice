from django.shortcuts import render

# Create your views here.
from django.template.context import RequestContext

def index(request):
   context = {'request': request, 'user': request.user}
   return render(request, 'airplane/index.html', context)