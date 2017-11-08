from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

