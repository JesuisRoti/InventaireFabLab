from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('reservation/', views.reserver, name="reservation"),
    path('retour/', views.retour, name="retour"),
    path('error/', views.error, name="erreur"),
    path('success/', views.success, name="succes"),
    path('', views.home),
    path('search/', views.searchProduct, name="search"),
    path('pole/', views.show_pole),
    path('categorie/<str:categorie>', views.show_product),
    path('pole/<str:pole_name>',views.show_category),
    re_path(r'^ajout_produit/(?P<cat_name>.+)', views.ajout_Produit, name="nouveau_produit"),
    re_path(r'^login/(?P<cat_name>.+)', views.check_login, name="login_produit")
]
