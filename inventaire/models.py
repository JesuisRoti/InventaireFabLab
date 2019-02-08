from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class pole (models.Model):
    class Meta:
        verbose_name = _("Pôle")
    pole_Name = models.CharField(max_length=50)
    pole_Ref = models.CharField(max_length=30)

    def __int__(self):
        return self.id

class category (models.Model):
    class Meta:
        verbose_name = _("Catégorie")
    category_name = models.CharField(max_length=100)
    category_Ref = models.CharField(max_length=30)
    pole_id = models.ForeignKey('pole', on_delete=models.PROTECT)

    def __int__(self):
        return self.id

class product (models.Model):
    class Meta:
        verbose_name = _("Produit")
    product_Name = models.CharField(max_length=100, verbose_name="Nom du Produit")
    product_Ref = models.CharField(max_length=200)
    available_Product = models.PositiveIntegerField(null=True, verbose_name="Quantité Disponible")
    stock = models.PositiveIntegerField(null=True, verbose_name="Quantité Totale")
    id_Category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

    def __str__(self):
        return self.product_Name


class reservation (models.Model):
    class Meta:
        verbose_name = _("Réservation")
    first_Name = models.CharField(max_length=100, verbose_name = "Prénom")
    last_Name = models.CharField(max_length=100, verbose_name = "Nom")
    promotion_choice = (
        ('A1', 'Première Année'),
        ('A2', 'Deuxième Année'),
        ('A3', 'Troisième Année'),
        ('A4', 'Quatrième Année'),
        ('A5', 'Cinquieme Année'),
    )
    promotion = models.CharField(max_length=4, choices=promotion_choice, default='A1')
    starting_Date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField(null=False, verbose_name = "Quantité")
    return_Quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name = "Quantité rendue")
    return_Date = models.DateField(verbose_name = "Date de retour (jj/mm/aaaa)")
    id_Product = models.ForeignKey('product', on_delete=models.PROTECT, null=True, blank=True)

class project_List (models.Model):
    class Meta:
        verbose_name = _("Liste des projet")
    project_Name = models.CharField(max_length=100, verbose_name="Nom du projet")
    promotion_choice = (
        ('A1', 'Première Année'),
        ('A2', 'Deuxième Année'),
        ('A3', 'Troisième Année'),
        ('A4', 'Quatrième Année'),
        ('A5', 'Cinquieme Année'),
    )
    promotion = models.CharField(max_length=4, choices=promotion_choice, default='A1')
    duration = models.PositiveIntegerField(null=False, verbose_name = "Durée du projet")

    def __str__(self):
        return self.project_Name

class stock_modification (models.Model):
    class Meta:
        verbose_name = _("Historique des modification")
    first_Name = models.CharField(max_length=100, verbose_name="Prénom")
    last_Name = models.CharField(max_length=100, verbose_name="Nom")
    comment = models.CharField(max_length=400, blank=True, verbose_name="Commentaire")
    name_Product = models.CharField(max_length=100, verbose_name="Nom du Produit")
    modification = models.CharField(max_length=100)

class project_Reservation (models.Model):
    class Meta:
        verbose_name = _("Réservations des projet")
    first_Name = models.CharField(max_length=100, blank=True, verbose_name = "Prénom")
    last_Name = models.CharField(max_length=100, blank = True, verbose_name = "Nom")
    promotion_choice = (
        ('A1', 'Première Année'),
        ('A2', 'Deuxième Année'),
        ('A3', 'Troisième Année'),
        ('A4', 'Quatrième Année'),
        ('A5', 'Cinquieme Année'),
    )
    promotion = models.CharField(max_length=4, choices=promotion_choice, default='A1')
    starting_Date = models.DateField(blank = True, null = True)
    return_Date = models.DateField(blank=True, null = True)
    project_Name = models.ForeignKey('project_List', on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class project_material (models.Model):
    class Meta:
        verbose_name = _("Matériaux des projet")
    project_Name = models.ForeignKey('project_List', on_delete=models.CASCADE)
    id_Product = models.ForeignKey('product', on_delete=models.CASCADE, verbose_name = "Nom du Produit")
    quantity = models.PositiveIntegerField(null=False, verbose_name = "Quantité")

class project_reservation_material (models.Model):
    class Meta:
        verbose_name = _("Réservation des matériaux des projet")
    id_Project_Reservation = models.ForeignKey('project_Reservation', on_delete=models.CASCADE)
    id_Product = models.ForeignKey('product', on_delete=models.CASCADE, verbose_name = "Nom du Produit")
    quantity = models.PositiveIntegerField(null=False, verbose_name = "Quantité")
    return_Quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name = "Quantité rendue")
    return_Date = models.DateField(null=True, blank=True)


class security_article (models.Model):
    class Meta:
        verbose_name = _("Fiche de sécurité")
        verbose_name_plural = _("Fiches de sécurité")
    title = models.CharField(max_length=50, verbose_name = "Titre")
    article = models.TextField(max_length=4000, verbose_name = "Contenu")
    date = models.DateField(auto_now=True)
    show_it = models.BooleanField(verbose_name = "Visible")

class profession_article (models.Model):
    class Meta:
        verbose_name = _("Fiche métier")
        verbose_name_plural = _("Fiches métier")
    title = models.CharField(max_length=50, verbose_name = "Titre")
    article = models.TextField(max_length=4000, verbose_name = "Contenu")
    date = models.DateField(auto_now=True)
    show_it = models.BooleanField(verbose_name = "Affiché")

class news_article (models.Model):
    class Meta:
        verbose_name = _("Fiche d'actualité")
        verbose_name_plural = _("Fiches d'actualité")
    title = models.CharField(max_length=50, verbose_name = "Titre")
    article = models.TextField(max_length=4000, verbose_name = "Contenu")
    date = models.DateField(auto_now=True)
    show_it = models.BooleanField(verbose_name = "Affiché")


