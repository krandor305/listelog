from django.db import models
from bde.models import bde
from utilapp.models import etudiant

class Messagebde(models.Model):
    etudiantc=models.ForeignKey(etudiant,on_delete=models.DO_NOTHING)
    bdec=models.ForeignKey(bde,on_delete=models.CASCADE)
    anonymat=models.BooleanField(default=False)
    contenu=models.TextField(max_length=2000)

    def __str__(self):
        return self.bdec

