from django.shortcuts import render
from bdeapps.views import checkperm
from .forms import ajoutsection
from .models import section
from bde.models import bde
from django.http import HttpResponseNotFound

def ajoutsectionview(request):
    if request.user.is_authenticated and (request.user.etudiant.poste=='President' or checkperm(request.user.etudiant,"allowed_section")):
        form=ajoutsection()
        if request.method=='POST':
            form=ajoutsection(request.POST)
            if form.is_valid():#url ne doit pas contenir d'espaces
                form.instance.bde=request.user.etudiant.bdechoisi
                form.save()
        return render(request,'websites/ajoutsection.html',{'form':form,'user':request.user.etudiant})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def showsite(request,nomasso,nomsection):
    try:
        selectionsection=section.objects.get(titre=nomsection,bde=bde.objects.get(nom=nomasso))
        sections=section.objects.all()
        return render(request,'websites/showsite.html',{"sections":sections,"selection":selectionsection})
    except section.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')


