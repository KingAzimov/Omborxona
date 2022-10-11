from django.contrib.auth.models import User
from django.db import models

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=90)
    tel = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vazifa = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.ism}, {self.nom}, {self.manzil}"