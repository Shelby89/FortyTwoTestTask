from django.shortcuts import render
from django.conf.urls import patterns, url

from apps.hello import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

# Create your views here.
