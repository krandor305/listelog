from . import models
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from django.forms import widgets

class ajoutsection(ModelForm):
    class Meta:
        model=models.section
        exclude=['bde']
