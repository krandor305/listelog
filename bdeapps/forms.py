from . import models
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from utilapp.models import Permissionsbde,etudiant
from django.forms import widgets

class TresoOpForm(forms.Form):
    titre=forms.CharField(max_length=50)
    MontantEntrée=forms.DecimalField(max_digits=10,decimal_places=2,required=False,label="Montant entrée")
    MontantSortie=forms.DecimalField(max_digits=10,decimal_places=2,required=False,label="Montant Sortie")

class ChangePerms(forms.ModelForm):
    class Meta:
        model=etudiant
        fields=['permissions_bde']
        widgets = {
            'permissions_bde': forms.CheckboxSelectMultiple,
        }

class AjoutEvent(forms.ModelForm):
    class Meta:
        model=models.event
        exclude=['organisateur']
    widgets = {
            'date' : forms.DateInput(attrs={'type':'date'}),
            'invites': forms.CheckboxSelectMultiple,
        }

class AjoutMission(forms.ModelForm):
    class Meta:
        model=models.mission
        exclude=['pour_bde']

class modifMission(forms.ModelForm):
    class Meta:
        model=models.mission
        exclude=['pour_bde','par_utilisateur']


class Ajoutnews(forms.ModelForm):
    class Meta:
        model=models.newsasso
        exclude=['bde']

