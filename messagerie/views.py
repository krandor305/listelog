from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import messageForm
from .models import Messagebde

def chatbde(request):
    if request.user.is_authenticated and request.user.etudiant.bdechoisi is not None:
        messages = Messagebde.objects.filter(bdec=request.user.etudiant.bdechoisi)
        if request.method=='POST':
            form=messageForm(request.POST)
            if form.is_valid():
                Message=Messagebde(contenu=form.cleaned_data["contenu"],anonymat=form.cleaned_data["anonymat"],etudiantc=request.user.etudiant,bdec=request.user.etudiant.bdechoisi)
                Message.save()
        else:
            form=messageForm()
        return render(request,'messagerie/chatbde.html',{"form":form,"messages":messages,"user":request.user.etudiant})
    else:
        return HttpResponseRedirect("/")#veuillez d'abord vous connecter ou rejoindre un bde


