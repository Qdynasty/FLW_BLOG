from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,HttpResponse
def index(request):
    return render(request,template_name ='Html/index.html')

