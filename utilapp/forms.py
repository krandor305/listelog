from . import models
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets


class LoginForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur",max_length=60)
    password=forms.CharField(label="Mot De Passe",widget=forms.PasswordInput)
    prenom=forms.CharField(label="Prenom",max_length=60)
    nom=forms.CharField(label="Nom",max_length=60)
    mail=forms.CharField(label="Adresse mail",max_length=60,required=True)

class LoginUser(forms.Form):
    username=forms.CharField(max_length=60)
    password=forms.CharField(widget=forms.PasswordInput)

class changeuser(ModelForm):
    class Meta:
        model=models.etudiant
        fields=['first_name','last_name','image']

class ModmdpEtudiant(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput)

class sendmail(forms.Form):
    mail=forms.EmailField(label="Votre mail")
