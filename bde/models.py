from django.db import models
from django.contrib.auth.models import User

class bde(models.Model):
    nom=models.CharField(max_length=30,unique=True)
    image=models.ImageField(upload_to="bde_images",default="media/defaultbde.png",null=True)
    etablissement=models.CharField(max_length=60,null=True)
    adresse=models.CharField(max_length=60,null=True)

    def __str__(self):
            return self.nom

class News(models.Model):
    Titre=models.CharField(max_length=50)
    Description=models.TextField(max_length=300)
    image=models.ImageField(upload_to="news_images",default="media/defaultbde.png",null=True)
    T1=models.CharField(max_length=50)
    D2=models.TextField(max_length=300)

    def __str__(self):
        return self.Titre
    






