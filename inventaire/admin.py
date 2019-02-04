from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from inventaire.models import *
from import_export import resources

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_Name', 'last_Name', 'return_Date')

class PoleResource(resources.ModelResource):

    class Meta:
        model = pole


class CategoryResource(resources.ModelResource):

    class Meta:
        model = category


class ProductResource(resources.ModelResource):

    class Meta:
        model = product

@admin.register(pole)
class PoleAdmin(ImportExportModelAdmin):
    list_display = ('pole_Name', 'pole_Ref',)
    list_filter = ('pole_Name',)
    resource_class = PoleResource

@admin.register(category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('category_name', 'category_Ref', 'pole_id',)
    list_filter = ('pole_id',)
    resource_class = CategoryResource

@admin.register(product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('product_Name', 'product_Ref', 'available_Product', 'stock','id_Category',)
    list_filter = ('id_Category',)
    resource_class = ProductResource

class ProjectReservationMaterialAdmin(admin.ModelAdmin):
    list_display = ('id_Project_Reservation', 'id_Product', 'quantity')

class ProjectReservationAdmin(admin.ModelAdmin):
    list_display = ('last_Name', 'first_Name', 'project_Name')

class ProjectMaterialAdmin(admin.ModelAdmin):
    list_display = ('project_Name', 'id_Product', 'quantity')

# admin.site.register(pole)
# admin.site.register(product, ProduitAdmin)
admin.site.register(reservation, ReservationAdmin)
# admin.site.register(category)
admin.site.register(project_Reservation, ProjectReservationAdmin)
admin.site.register(project_List)
admin.site.register(stock_modification)
admin.site.register(project_reservation_material, ProjectReservationMaterialAdmin)
admin.site.register(project_material, ProjectMaterialAdmin)
admin.site.register(security_article)
admin.site.register(profession_article)
admin.site.register(news_article)
