from django.contrib import admin
from .models import Produit

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display =('nom', 'test')
    list_filter = ('nom', 'test')
    admin.site.site_header = 'Parametres'
    admin.site.site_title = 'Parametres'
    admin.site.index_title = 'FabLab'


admin.site.register(Produit, ProduitAdmin)