from django.conf.urls import url,include
from django.contrib import admin
from blog.views import index

urlpatterns = [
    #"""应用"""
    url(r'^/$', index)
]