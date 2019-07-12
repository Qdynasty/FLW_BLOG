from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,HttpResponse
def index(request):
    return HttpResponse("6666")