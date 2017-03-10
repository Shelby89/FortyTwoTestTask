from django.conf.urls import patterns, url
from apps.list_requests import views

urlpatterns = patterns(
    '',
    url(r'^$', views.list_requests, name='requests'),
)
