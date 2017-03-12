from django.conf.urls import patterns, url
from apps.edit import views
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', views.edit, name="edit"),
    url(r'edit_page', TemplateView.as_view(template_name="edit_page.html"), name="edit_page")
)
