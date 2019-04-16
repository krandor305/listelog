from django.db import models
from bde.models import bde
from utilapp.models import etudiant

class TresoOP(models.Model):
    bdeconcerne=models.ForeignKey(bde,on_delete=models.CASCADE)
    Montant=models.DecimalField(max_digits=10,decimal_places=2)
    dateop=models.DateField(auto_now_add=True)
    titre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.titre

class mission(models.Model):#besoin d'un abstractmodel
    Titre=models.CharField(max_length=25)
    Description=models.TextField(max_length=300)
    date=models.DateTimeField(blank=True,null=True)
    pour_bde=models.ForeignKey(bde,on_delete=models.CASCADE)
    par_utilisateur=models.ForeignKey(etudiant,on_delete=models.CASCADE)

    def __str__(self):
        return self.Titre

class event(models.Model):
    titre=models.CharField(max_length=30)
    Description=models.TextField(max_length=300)
    places=models.IntegerField()
    date=models.DateTimeField(blank=True,null=True)
    lieu=models.CharField(max_length=50)
    organisateur=models.ForeignKey(bde,on_delete=models.CASCADE)
    prive=models.BooleanField(default=False)
    type_evenement=models.CharField(max_length=30)
    invites=models.ManyToManyField(etudiant,blank=True)

    def __str__(self):
        return self.titre

class newsasso(models.Model):
    titre=models.CharField(max_length=30)
    Description=models.TextField(max_length=300)
    bde=models.OneToOneField(bde,on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Usermail(models.Model):
    email=models.EmailField(unique=False)
    event=models.ForeignKey(event,on_delete=models.CASCADE)


