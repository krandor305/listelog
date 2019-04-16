from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from . import forms
from . import models
from django.contrib.auth.models import User,Permission
from django.contrib.auth.decorators import login_required
from utilapp.models import etudiant,demandenom
from bdeapps.models import event,newsasso
from utilapp.views import onaddbde,offaddbde
from bdeapps.views import checkperm

def index(request):#affiche l'index 
    utilobj=None
    notif=notification(request)
    i=0
    news=models.News.objects.all()
    if notif != None:
        notif=notif.replace("_", " ")
    if request.user.is_authenticated:
        utilobj=request.user.etudiant
    return render(request,'bde/index.html',
    {'bde_liste':models.bde.objects.all(),'user':utilobj,'notification':notif,'news':news,'iter':i})#changer le get en polymorphisme

def notification(request):
    if 'connecte' in request.GET:
        return 'connecte'
    elif 'deconnecte' in request.GET:
        return 'deconnecte'
    elif 'vous_appartenez_deja_a_un_bde' in request.GET:
        return 'vous_appartenez_deja_a_un_bde'
    elif 'Veuillez_integrer_un_bde_ou_en_ajouter_un' in request.GET:
        return 'Veuillez_integrer_un_bde_ou_en_ajouter_un'
    elif 'veuillez_consulter_votre_mail' in request.GET:
        return 'veuillez_consulter_votre_mail'
    elif 'votre_compte_est_deja_actif' in request.GET:
        return 'votre compte est deja actif'
    elif "Veuillez_d'abord_quitter_votre_association" in request.GET:
        return "Veuillez_d'abord_quitter_votre_association"
    else:
        return None
        

def affichebde(request,slug):#affiche le bde
    utilobj=None
    if request.user.is_authenticated:
        utilobj=request.user.etudiant
    return render(request,'bde/detailbde.html',
    {"object":models.bde.objects.get(nom=slug),
    "user":utilobj})

def monbde(request):#affiche mon bde et demandeurs selon permission
    if request.user.is_authenticated and request.user.etudiant.bdechoisi is not None:
        demandeurs = []
        evenements=None
        allowed=checkperm(request.user.etudiant,"accepter_membre")
        allowedevent=checkperm(request.user.etudiant,"ajout_event")
        allowedmission=checkperm(request.user.etudiant,"donner_mission") 
        if (request.user.etudiant.poste == 'President') or (allowed == True):
            for etud in etudiant.objects.filter(bdechoisi=None):
                for asso in etud.demande_bde.all():
                    if asso==request.user.etudiant.bdechoisi:
                        demandeurs.append(etud)
                        break
        if (request.user.etudiant.poste == 'President') or (allowedevent == True):
            allowedevent=True
            evenements=event.objects.filter(organisateur=request.user.etudiant.bdechoisi)
        return render(request,'bde/monbde.html',
        {"object":request.user.etudiant.bdechoisi,
        "user":request.user.etudiant,
        "membres":etudiant.objects.filter(bdechoisi=request.user.etudiant.bdechoisi),
        "demandeurs":demandeurs,
        "evenements":evenements,
        "allowedevent":allowedevent,
        "allowedmission":allowedmission,
        "news":newsasso.objects.filter(bde=request.user.etudiant.bdechoisi)})
    else:
        return HttpResponseRedirect("/?Veuillez_integrer_un_bde_ou_en_ajouter_un")#veuillez integrer une asso


def accepter(request,slug):
    for perm in request.user.etudiant.permissions_bde.all():
        if perm.nom_perm == "accepter_membre":
            allowed=True
            break
    allowed=checkperm(request.user.etudiant,"accepter_membre")
    if (request.user.etudiant.poste == 'President') or (allowed == True):
        demandeur=etudiant.objects.get(username=slug)
        demandeur.bdechoisi=request.user.etudiant.bdechoisi
        demandeur.save()
        return HttpResponseRedirect("/monbde")
    else:
        return HttpResponseRedirect("/")

def ajoutbde(request):#meme que précedent mais pas generique
    if request.user.is_authenticated:
        if request.user.etudiant.bdechoisi is None:
            if request.method=='POST':
                form=forms.AjoutBde(request.POST)
                if form.is_valid() and not models.bde.objects.filter(nom=form.cleaned_data["nom"]).exists():
                    form.instance.user=request.user.etudiant
                    form.save()
                    return HttpResponseRedirect("/")
            else:
                form=forms.AjoutBde()
            return render(request,"bde/ajoutbde.html",{"form":form,"user":request.user.etudiant})  
        return HttpResponseRedirect("/?vous_appartenez_deja_a_un_bde")
    else:
        return HttpResponseRedirect("/login")

def demandesnomview(request):
    if request.user.is_authenticated and request.user.is_staff:
        objects=demandenom.objects.all()
        return render(request,'bde/acceptebde.html',{"noms":objects})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
        


def accepterbde(request,name):
    try:
        nom1=demandenom.objects.get(nom=name)
        if request.user.is_authenticated and request.user.is_staff:
            bde1=models.bde(nom=nom1.nom)
            bde1.save()
            nom1.user.bdechoisi=bde1
            nom1.user.demande_bde.clear()
            nom1.user.poste='President'
            nom1.user.etudiant.save()
            offaddbde(nom1.user)
            nom1.delete()
            return HttpResponseRedirect("/adminaccept")
    except demandenom.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')


"""class detailAffiche(generic.DetailView):#affiche un bde et ses details
    model=models.bde
    template_name = 'bde/detailbde.html'
    slug_field='nom'"""

"""class VueGaffiche(generic.ListView):#affiche tout les bde
    model=models.bde
    template_name = 'bde/vue_gaffiche.html'"""

"""class bdeCreation(PermissionRequiredMixin,generic.CreateView):#cree un bde avec les permissions
    model=models.bde
    fields= '__all__'
    template_name = 'bde/ajoutbde.html'
    success_url="/"
    permission_required = 'bde.can_add'

    def dispatch(self, request, *args, **kwargs):#l'utlisateur doit rejoindre ce bde,devenir l'admin et changer ses autorsations afin qu'il ne puisse plus ajouter d'autres bde
        if not self.has_permission() and not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)"""





        




