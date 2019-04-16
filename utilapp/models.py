from django.db import models
from django.contrib.auth.models import User,Permission
from bde.models import bde

POSTES=(
    ('President','President'),
    ('Tresorier','Tresorier'),
    ('Membre','Membre'),
)

class Permissionsbde(models.Model):
    nom_perm=models.CharField(max_length=30)

    def __str__(self):
        return self.nom_perm

class etudiant(User):
    image=models.ImageField(upload_to='imagesetudiant',default='media/default.png')
    bdechoisi=models.ForeignKey(bde,blank=True,null=True,on_delete=models.DO_NOTHING)
    demande_bde=models.ManyToManyField(bde, blank=True ,related_name="demande")
    etablissement=models.CharField(max_length=30)
    poste=models.CharField(max_length=15,choices=POSTES,blank=True,null=True)
    permissions_bde=models.ManyToManyField(Permissionsbde,blank=True)

class demandenom(models.Model):
    nom=models.CharField(max_length=30)
    user=models.OneToOneField(etudiant,on_delete=models.CASCADE)

    