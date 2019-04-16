from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
      path('', views.index),
      path('ajoutbde/',views.ajoutbde),
      path('monbde/',views.monbde),
      path('accepter/<slug:slug>/',views.accepter),
      path('adminaccept/',views.demandesnomview),
      path('adminacceptbde/<name>/',views.accepterbde),
      path('voirbde/<slug:slug>/',views.affichebde, name='bde-detail'),
]

if settings.DEBUG:
    urlpatterns += [
 url(r'^media/(?P<path>.*)$', serve,
 {'document_root': settings.MEDIA_ROOT,}),
 ]