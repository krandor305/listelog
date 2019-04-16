from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('ajout',views.ajoutsectionview),
    path('<nomasso>/<nomsection>',views.showsite),
]

if settings.DEBUG:
    urlpatterns += [
 url(r'^media/(?P<path>.*)$', serve,
 {'document_root': settings.MEDIA_ROOT,}),
 ]