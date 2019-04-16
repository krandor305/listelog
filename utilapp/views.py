from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,Http404
from . import forms
from . import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User,Permission
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views import generic
from bde.models import bde
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.core.mail import send_mail,get_connection

def signup(request):#inscrit un utilisateur
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=forms.LoginForm(request.POST)
            if form.is_valid():
                if models.etudiant.objects.filter(username=form.cleaned_data['username']).exists() or models.etudiant.objects.filter(email=form.cleaned_data['mail'],is_active=True).exists():
                    return HttpResponseRedirect("/signup")#cet utilisateur existe deja
                etudiant=models.etudiant.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                etudiant.first_name=form.cleaned_data['prenom']
                etudiant.last_name=form.cleaned_data['nom']
                etudiant.email=form.cleaned_data['mail']
                etudiant.is_active = False
                onaddbde(etudiant)
                Token=PasswordResetTokenGenerator().make_token(etudiant)
                con=get_connection('django.core.mail.backends.console.EmailBackend')
                send_mail('Mot de passe','Here is the token:veriflogin/'+Token,'al-had@hotmail.com',[form.cleaned_data['mail']],fail_silently=False,connection=con)
                return HttpResponseRedirect("/?veuillez_consulter_votre_mail")
        else:
            form=forms.LoginForm()
        return render(request,'utilapp/inscription.html',{'form':form})
    else:
        HttpResponseRedirect("/")

def loginviewverif(request,slug):#connecte un utilisateur
    if not request.user.is_authenticated:
        if request.method =='POST':
            form=forms.LoginUser(request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if not user.is_active and PasswordResetTokenGenerator().check_token(user,slug):
                    user.is_active=True
                    user.save()
                    login(request,user)
                    for deluser in models.etudiant.objects.filter(email=user.email):
                        deluser.delete()
                    return HttpResponseRedirect('/?connecte=True')
                else:
                    return HttpResponseRedirect("/?votre_compte_est_deja_actif")
        else:
            form=forms.LoginUser()
        return render(request,'utilapp/login.html',{'form':form})
    else:
        return HttpResponseRedirect("/")#vous etes deja connecté 

def sendtokenforget(request):
    problem=False
    util=None
    if request.method=='POST':
        form=forms.sendmail(request.POST)
        if form.is_valid():
            try:
                util=models.etudiant.objects.get(email=form.cleaned_data['mail'],is_active=False)
                Token=PasswordResetTokenGenerator().make_token(util)
                con=get_connection('django.core.mail.backends.console.EmailBackend')
                send_mail('Mot de passe','Here is the token:veriflogin/'+Token,'al-had@hotmail.com',[form.cleaned_data['mail']],fail_silently=False,connection=con)
                return HttpResponseRedirect("/?veuillez_consulter_votre_mail")
            except models.etudiant.DoesNotExist:
                problem=True
    else:
        form=forms.sendmail()
    return render(request,'utilapp/envoicodemail.html',{"problem":problem,"form":form})

def loginview(request):#connecte un utilisateur
    if not request.user.is_authenticated:   
        if request.method =='POST':
            form=forms.LoginUser(request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'],is_active=False)
                if (user is not None and not user.is_staff and user.is_active):
                    login(request,user)
                    return HttpResponseRedirect('/?connecte=True')
        else:
            form=forms.LoginUser()
        return render(request,'utilapp/login.html',{'form':form})
    else:
        return HttpResponseRedirect("/")#vous etes deja connecté       


def sendtoken(request):
    if request.user.is_authenticated:
        Token=PasswordResetTokenGenerator().make_token(request.user)
        con=get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail('Mot de passe','Here is the token:changepwd/'+Token,'al-had@hotmail.com',[request.user.email],fail_silently=False,connection=con)
        return HttpResponseRedirect("/?veuillez_consulter_votre_mail")


def checktokenmdp(request,slug):#faire la meme pour la verification mail unique=true
    if request.user.is_authenticated and PasswordResetTokenGenerator().check_token(request.user,slug):
        if request.method=='POST':
            form=forms.ModmdpEtudiant(request.POST)
            if form.is_valid():
                request.user.password=form.cleaned_data['password']
                request.user.save()
                logout(request)
                return HttpResponseRedirect("/login")
        else:
            form=forms.ModmdpEtudiant(request.POST)
        return render(request,'utilapp/changemdp.html',{"form":form,"user":request.user.etudiant})



@login_required
def logoutview(request):#deconnecte l'utilisateur actuel
    logout(request)
    return HttpResponseRedirect('/?deconnecte=True')#vous vous etes deconnecté

def detailuser(request,slug):#checké
    utilobject=models.etudiant.objects.get(username=slug)
    form=None
    if request.user.is_authenticated and request.user.etudiant==utilobject:
        form=forms.changeuser(instance=utilobject)
        if request.method=='POST':
            form=forms.changeuser(request.POST,request.FILES,instance=utilobject)
            if form.is_valid():
                form.save()
    return render(request,'utilapp/detailuser.html',{"object":models.etudiant.objects.get(username=slug),
    "user":utilobject,"form":form})

@login_required
def demandebde(request,bdename):
    utilobject=request.user.etudiant
    if utilobject.bdechoisi is None:
        for bd in bde.objects.all():
            if str(bd)==bdename:
                utilobject.demande_bde.add(bd)
                utilobject.save()
                return HttpResponseRedirect("/")
    return HttpResponseRedirect("/?vous_appartenez_deja_a_un_bde")#vous avez deja un bde

@login_required   
def quittebde(request):#l'utilisateur actuel quitte le bde
    use1=request.user.etudiant
    if use1.bdechoisi is not None:
        use1.bdechoisi=None
        onaddbde(use1)
        use1.poste=None
        use1.permissions_bde.clear()
        use1.save()
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/?Veuillez_integrer_un_bde_ou_en_ajouter_un")#vous n'avez aucun bde a quitter

def surete(request):
    if request.user.is_authenticated:
        return render(request,'utilapp/surete.html',{"user":request.user.etudiant})
    else:
        return HttpResponseRedirect("/login")

def desacitvercpt(request):
    if request.user.is_authenticated:
        if request.user.etudiant.bdechoisi is None:            
            user=request.user
            logout(request)
            user.delete()
        else:
            return HttpResponseRedirect("/?Veuillez_d'abord_quitter_votre_association")
    return HttpResponseRedirect("/login")

def onaddbde(user):
    user.user_permissions.add(Permission.objects.get(name='Can add bde'))
    user.save()

def offaddbde(user):
    user.user_permissions.remove(Permission.objects.get(name='Can add bde'))
    user.save()      

