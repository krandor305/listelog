from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('tresorerie',views.tresoview),
    path('membre/<slug:slug>',views.voirmembre),
    path('passation/<slug:slug>',views.passationpresident),
    path('ajoutevent',views.addevent),
    path('event/<bdename>/<eventname>',views.showevent),
    path('deleteevent/<eventname>',views.deleteevent),
    path('donner_mission',views.donnermission),
    path('deltreso/<id>',views.deltreso),
    path('ajout_news',views.ajoutnews),
    path('modif_news/<bde1>/<Titre>',views.modifnews),
    path('suppr_news/<bde1>/<Titre>',views.deletenews),
]

if settings.DEBUG:
    urlpatterns += [
 url(r'^media/(?P<path>.*)$', serve,
 {'document_root': settings.MEDIA_ROOT,}),
 ]