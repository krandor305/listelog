from . import models
from django.forms import ModelForm
from django import forms
from utilapp.models import demandenom
from django.contrib.admin import widgets

class bdeForm(ModelForm):
    class Meta:
        model=models.bde
        fields = '__all__'

class AjoutBde(ModelForm):
    class Meta:
        model=demandenom
        fields=['nom']