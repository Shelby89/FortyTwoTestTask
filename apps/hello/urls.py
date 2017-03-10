from django.conf.urls import patterns, url
from apps.hello import views


urlpatterns = patterns('',
                       url(r'start_page/$', views.start_page, name="start_page"),
                       )
