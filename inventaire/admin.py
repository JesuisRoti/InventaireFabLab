from django.contrib import admin
from .models import *

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    list_display =('product_Name', 'product_Ref', 'available_Product', 'stock')
    list_filter = ('product_Name',)
    admin.site.site_header = 'Parametres'
    admin.site.site_title = 'Parametres'
    admin.site.index_title = 'FabLab'

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_Name', 'last_Name', 'return_Date')


admin.site.register(pole)
admin.site.register(product, ProduitAdmin)
admin.site.register(reservation, ReservationAdmin)
admin.site.register(category)
admin.site.register(project_Reservation)
admin.site.register(project_List)
admin.site.register(stock_modification)
admin.site.register(project_reservation_material)
admin.site.register(project_material)
admin.site.register(security_article)
admin.site.register(profession_article)
admin.site.register(news_article)
