from django.shortcuts import render
from .models import TresoOP,event,mission,newsasso
from .forms import TresoOpForm,ChangePerms,AjoutEvent,AjoutMission,modifMission,Ajoutnews
from django import forms
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from utilapp.models import etudiant
from utilapp.views import offaddbde
from bde.models import bde
from django.forms import modelformset_factory

#tresoOP
def tresoview(request):
    if request.user.is_authenticated and request.user.etudiant.bdechoisi is not None:
        tresorerie=TresoOP.objects.filter(bdeconcerne=request.user.etudiant.bdechoisi)
        allowed=checkperm(request.user.etudiant,"changer_treso")
        if (allowed==True) or (request.user.etudiant.poste == 'President') or (request.user.etudiant.poste == 'Tresorier'):
            allowed=True
            if request.method=='POST':
                form=TresoOpForm(request.POST)
                if form.is_valid():
                    entree=form.cleaned_data['MontantEntrée']
                    sortie=form.cleaned_data['MontantSortie']
                    if entree is not None:
                        obj=TresoOP(bdeconcerne=request.user.etudiant.bdechoisi,Montant=entree,titre=form.cleaned_data['titre'])
                        obj.save()
                    if sortie is not None:
                        obj=TresoOP(bdeconcerne=request.user.etudiant.bdechoisi,Montant=-sortie,titre=form.cleaned_data['titre'])
                        obj.save()
            else:
                form=TresoOpForm()
        return render(request,'bdeapps/tresorerie.html',{"form":form,"tresorerie":tresorerie,"user":request.user.etudiant,"allowed":allowed})
    else:
        return HttpResponseRedirect("/")#veuillez rejoindre une asso

def deltreso(request,id):
    try:
        operation=TresoOP.objects.get(pk=id,bdeconcerne=request.user.etudiant.bdechoisi)
        if request.user.etudiant.is_authenticated and (request.user.etudiant.poste=='President' or request.user.etudiant.poste=='Tresorier' or checkperm(request.user.etudiant,"changer_treso")):
            operation.delete()
            return HttpResponseRedirect("/bde/tresorerie")
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    except TresoOP.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

#membre
def voirmembre(request,slug):
    if request.user.is_authenticated:
        try:
            membre=etudiant.objects.get(username=slug,bdechoisi=request.user.etudiant.bdechoisi)
        except etudiant.DoesNotExist:
            return HttpResponseNotFound('<h1>Page not found</h1>')#cet utilisateur n'appartient pas a votre asso
        form=None
        allowed=checkperm(request.user.etudiant,"changer_perm")
        if (request.user.etudiant.poste == 'President') or (allowed==True):
            allowed=True
            if request.method=='POST':
                form=ChangePerms(request.POST,instance=membre)
                if form.is_valid():
                    form.save()
            else:
                form=ChangePerms(instance=membre)
        missions=None
        allowedmission=False
        if mission.objects.filter(par_utilisateur=membre).exists() and (request.user.etudiant.username==slug or request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"donner_mission")):
            if request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"donner_mission"):
                allowedmission=True
                formmission=modelformset_factory(mission,form=modifMission,extra=0)
                missions=formmission(request.POST or None,queryset=mission.objects.filter(par_utilisateur=membre))
                if request.method=='POST':
                    if missions.is_valid():
                        for forminst in missions:
                            if forminst.is_valid():
                                instance=forminst.save(commit=False)
                                instance.save()
            else:
                missions=mission.objects.filter(par_utilisateur=membre)
        return render(request,'bdeapps/membre.html',{"membre":membre,"user":request.user.etudiant,"form1":form,"allowed":allowed,"missions":missions,"allowedmission":allowedmission})
    else:
        return HttpResponseRedirect("/login")#connectez vous

def passationpresident(request,slug):
    try:
        successeur=etudiant.objects.get(bdechoisi=request.user.etudiant.bdechoisi,username=slug)
        if request.user.is_authenticated and request.user.etudiant.bdechoisi=='President' and request.user.etudiant != successeur:
            successeur.poste='President'
            request.user.etudiant.poste='Membre'
            successeur.save()
            request.user.etudiant.save()
            return HttpResponseRedirect("/monbde")#success 
    except etudiant.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')#no success

#event
def addevent(request):
    allowed=checkperm(request.user.etudiant,"ajout_event")
    if request.user.is_authenticated and ((request.user.etudiant.poste == 'President') or (allowed==True)):
        allowed=True
        form=AjoutEvent()
        if 'q' in request.GET:
            try:
                evenement=event.objects.get(titre=request.GET['q'],organisateur=request.user.etudiant.bdechoisi)
                form=AjoutEvent(instance=evenement)
            except event.DoesNotExist:
                return HttpResponseNotFound('<h1>Page not found</h1>')
        if request.method=='POST':
            form=AjoutEvent(request.POST)
            if form.is_valid() and not event.objects.filter(organisateur=request.user.etudiant.bdechoisi,titre=form.cleaned_data['titre']).exists():
                form.instance.organisateur=request.user.etudiant.bdechoisi
                form.save()
                return HttpResponseRedirect('/bde/event/'+str(request.user.etudiant.bdechoisi)+'/'+form.instance.titre)
        return render(request,'bdeapps/ajoutevent.html',{"form":form,"user":request.user.etudiant})
    else:
        return HttpResponseRedirect("/monbde")#vous_n'avez_pas_la_permission_d'effectuer_cette_action

def showevent(request,bdename,eventname):
    try:
        evenement=event.objects.get(organisateur=bde.objects.get(nom=bdename),titre=eventname)
        allowed=checkperm(request.user.etudiant,"ajout_event")
        form=None
        if evenement.prive==False or request.user.etudiant.bdechoisi==evenement.organisateur:
            if request.user.is_authenticated and request.user.etudiant.bdechoisi==evenement.organisateur and ((request.user.etudiant.poste == 'President') or (allowed==True)):
                allowed=True
                form=AjoutEvent(instance=evenement)
                if request.method=='POST':
                    form=AjoutEvent(request.POST,instance=evenement)
                    if form.is_valid() and (not event.objects.filter(organisateur=request.user.etudiant.bdechoisi,titre=form.cleaned_data['titre']).exists() or form.cleaned_data['titre']==evenement.titre):
                        form.save()
            return render(request,'bdeapps/showevent.html',{"user":request.user.etudiant,"form":form,"allowed":allowed,"evenement":evenement})
        else:
            return HttpResponseRedirect("/")
    except event.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def deleteevent(request,eventname):
    try:
        evenement=event.objects.get(organisateur=request.user.etudiant.bdechoisi,titre=eventname)
        allowed=checkperm(request.user.etudiant,"ajout_event")
        if request.user.is_authenticated and request.user.etudiant.bdechoisi==evenement.organisateur and ((request.user.etudiant.poste == 'President') or (allowed==True)):
            evenement.delete()
            return HttpResponseRedirect("/monbde")
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    except event.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

#mission(reste modifiermission,supprimmer mission)
def donnermission(request):
    if request.user.is_authenticated and (request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"donner_mission")):
        form=AjoutMission()
        form.fields["par_utilisateur"].queryset = etudiant.objects.filter(bdechoisi=request.user.etudiant.bdechoisi)
        if request.method=='POST':
            form=AjoutMission(request.POST)
            if form.is_valid():
                form.instance.pour_bde=request.user.etudiant.bdechoisi
                form.save()
                return HttpResponseRedirect("/monbde")
        return render(request,'bdeapps/donmission.html',{"form":form,"user":request.user.etudiant})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def ajoutnews(request):
    if request.user.is_authenticated and (request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"ajout_news")):
        if request.method=='POST':
            form=Ajoutnews(request.POST)
            if form.is_valid():
                form.instance.bde=request.user.etudiant.bdechoisi
                form.save()
        else:
            form=Ajoutnews()
        return render(request,'bdeapps/ajoutnews.html',{"form":form,"user":request.user.etudiant})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
        
def modifnews(request,bde1,Titre):
    try:
        new=newsasso.objects.get(titre=Titre,bde=bde.objects.get(nom=bde1))
        if request.user.is_authenticated and (request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"ajout_news")): 
            if request.method=='POST':
                form=Ajoutnews(request.POST,instance=new)
                if form.is_valid():
                    form.save()
            else:
                form=Ajoutnews(instance=new)
            return render(request,'bdeapps/modifnews.html',{"form":form,"user":request.user.etudiant})
    except newsasso.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def deletenews(request,bde1,Titre):
    try:
        new=newsasso.objects.get(titre=Titre,bde=bde.objects.get(nom=bde1))
        if request.user.is_authenticated and (request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"ajout_news")):
            new.delete()
            return HttpResponseRedirect("/monbde") 
    except newsasso.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')
        

def checkperm(user,permission):
    for perm in user.permissions_bde.all():
        if perm.nom_perm == permission:
            return True
    return False






