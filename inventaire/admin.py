from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from inventaire.models import *
from import_export import resources
from import_export.formats import base_formats

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

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
        )
        return [f for f in formats if f().can_import()]


@admin.register(category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('category_name', 'category_Ref', 'pole_id',)
    list_filter = ('pole_id',)
    resource_class = CategoryResource

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
        )
        return [f for f in formats if f().can_import()]


@admin.register(product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('product_Name', 'product_Ref', 'available_Product', 'stock','id_Category',)
    list_filter = ('id_Category',)
    resource_class = ProductResource

    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
        )
        return [f for f in formats if f().can_export()]

    def get_import_formats(self):
        """
        Returns available export formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
        )
        return [f for f in formats if f().can_import()]


class ProjectReservationMaterialAdmin(admin.ModelAdmin):
    list_display = ('id_Project_Reservation', 'id_Product', 'quantity')

class ProjectReservationAdmin(admin.ModelAdmin):
    list_display = ('last_Name', 'first_Name', 'project_Name')

class ProjectMaterialAdmin(admin.ModelAdmin):
    list_display = ('project_Name', 'id_Product', 'quantity')

class SecurityArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'show_it')

class ProfessionArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'show_it')

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'show_it')

class StockModificationAdmin(admin.ModelAdmin):
    list_display = ('first_Name', 'name_Product', 'modification')

admin.site.register(reservation, ReservationAdmin)
admin.site.register(project_Reservation, ProjectReservationAdmin)
admin.site.register(project_List)
admin.site.register(stock_modification, StockModificationAdmin)
admin.site.register(project_reservation_material, ProjectReservationMaterialAdmin)
admin.site.register(project_material, ProjectMaterialAdmin)
admin.site.register(security_article, SecurityArticleAdmin)
admin.site.register(profession_article, ProfessionArticleAdmin)
admin.site.register(news_article, NewsArticleAdmin)
