from django.conf.urls import patterns, url
from apps.edit import views


urlpatterns = patterns(
    '',
    url(r'^$', views.edit, name='edit'),
)