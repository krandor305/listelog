from django.db import models
from bde.models import bde

class section(models.Model):
    titre=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    contenu=models.TextField(max_length=3000)
    bde=models.ForeignKey(bde,on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

