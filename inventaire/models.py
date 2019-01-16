from django.db import models

# Create your models here.

class pole (models.Model):
    pole_Name = models.CharField(max_length=50)

    def __int__(self):
        return self.id

class category (models.Model):
    category_name = models.CharField(max_length=100)
    pole_id = models.ForeignKey('pole', on_delete=models.PROTECT)

    def __int__(self):
        return self.id

class product (models.Model):
    product_Name = models.CharField(max_length=100)
    product_Ref = models.CharField(max_length=200)
    available_Product = models.PositiveIntegerField(null=True)
    stock = models.PositiveIntegerField(null=True)
    id_Category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class reservation (models.Model):
    first_Name = models.CharField(max_length=100, verbose_name = "Prénom")
    last_Name = models.CharField(max_length=100, verbose_name = "Nom")
    promotion_choice = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
    )
    promotion = models.CharField(max_length=4, choices=promotion_choice, default='A1')
    starting_Date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField(null=False, verbose_name = "Quantité")
    return_Quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name = "Quantité rendue")
    return_Date = models.DateField(null=True, blank=True, verbose_name = "Date de retour")
    id_Product = models.ForeignKey('product', on_delete=models.PROTECT, null=True, blank=True)

class project_List (models.Model):
    project_Name = models.CharField(max_length=100, verbose_name = "Nom du projet")
    promotion_choice = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
    )
    promotion = models.CharField(max_length=4, choices=promotion_choice, default='A1')
    duration = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.project_Name

class stock_modification (models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    comment = models.CharField(max_length=400)
    id_Product = models.IntegerField()
    name_Product = models.CharField(max_length=100)
    modification = models.CharField(max_length=100)

class project_Reservation (models.Model):
    last_Name = models.CharField(max_length=100)
    first_Name = models.CharField(max_length=100)
    promotion_choice = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
    )
    promotion = models.CharField(max_length=4, choices=promotion_choice, default='A1')
    starting_Date = models.DateField()
    return_Date = models.DateField(blank=True)

    def __str__(self):
        return self.id

class project_material (models.Model):
    project_Name = models.ForeignKey('project_List', on_delete=models.PROTECT)
    id_Product = models.ForeignKey('product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=False)

class project_reservation_material (models.Model):
    id_Project_Reservation = models.ForeignKey('project_Reservation', on_delete=models.PROTECT)
    id_Product = models.ForeignKey('product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(null=False)
    return_Quantity = models.PositiveIntegerField(null=True)
    return_Date = models.DateField(blank=True)


class security_article (models.Model):
    title = models.CharField(max_length=50)
    article = models.CharField(max_length=4000)
    date = models.DateField(auto_now=True)
    show_it = models.BooleanField()

class profession_article (models.Model):
    title = models.CharField(max_length=50)
    article = models.CharField(max_length=4000)
    date = models.DateField(auto_now=True)
    show_it = models.BooleanField()

class news_article (models.Model):
    title = models.CharField(max_length=50)
    article = models.CharField(max_length=4000)
    date = models.DateField(auto_now=True)
    show_it = models.BooleanField()


