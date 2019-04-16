from . import models
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets

class messageForm(ModelForm):
    class Meta:
        model=models.Messagebde
        fields=['anonymat','contenu']
