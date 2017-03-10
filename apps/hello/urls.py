from django.conf.urls import patterns, url
from apps.hello import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'start_page/$', views.start_page, name="start_page"),
    url(r'requests_page/$', views.requests_page, name="requests_page"),
    )
