from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
      path('signup/',views.signup),
      path('logout',views.logoutview),
      path('login/',views.loginview),
      path('demande/<bdename>/',views.demandebde),
      path('quit',views.quittebde),
      path('surete',views.surete),
      path('Supprimercompte',views.desacitvercpt),
      path('Passwordreinit',views.sendtoken),#envoie le mail pour reinit le mdp
      path('veriflogin/<slug>/',views.loginviewverif),#un login pour ceux qui ont le lien
      path('changepwd/<slug>/',views.checktokenmdp),#changelemot de passe avec un slug dans l'url
      path('renvoitoken/',views.sendtokenforget),
      path('user/<slug:slug>/',views.detailuser, name='user-detail'),
]

if settings.DEBUG:
    urlpatterns += [
 url(r'^media/(?P<path>.*)$', serve,
 {'document_root': settings.MEDIA_ROOT,}),
 ]