from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bde.urls')),
    path('', include('utilapp.urls')),
    path('rooms/', include('messagerie.urls')),
    path('bde/', include('bdeapps.urls')),
    path('site/', include('websites.urls')),
]

if settings.DEBUG:
    urlpatterns += [
 url(r'^media/(?P<path>.*)$', serve,
 {'document_root': settings.MEDIA_ROOT,}),
 ]