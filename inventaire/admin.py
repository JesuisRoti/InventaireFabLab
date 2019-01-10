from django.contrib import admin
from .models import *

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display =('product_Name', 'product_Ref', 'available_Product', 'stock')
    list_filter = ('product_Name',)
    admin.site.site_header = 'Parametres'
    admin.site.site_title = 'Parametres'
    admin.site.index_title = 'FabLab'


admin.site.register(product, ProduitAdmin)
admin.site.register(reservation)
admin.site.register(category)
admin.site.register(project_Reservation)
admin.site.register(project_List)
admin.site.register(stock_modification)
admin.site.register(project_reservation_material)
admin.site.register(project_material)
