from django.db import models

# Create your models here.

class Produit (models.Model):
    nom = models.CharField(max_length=100)
    test = models.PositiveIntegerField(null=True)
    categorie = models.PositiveIntegerField()
