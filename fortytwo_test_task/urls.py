from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('apps.hello.urls', namespace="hello")),
    url(r'^start_page/', 'apps.hello.views.start_page', name="start_page"),
    url(
        r'^requests/',
        include('apps.list_requests.urls', namespace="list_requests")
    ),
    url(
        r'^requests/table/', 'apps.list_requests.views.table', name="table"
    ),
    
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
