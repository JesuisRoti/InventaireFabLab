from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation/', views.reserver, name="reservation"),
    path('retour/', views.retour, name="retour"),
    path('error/', views.error, name="erreur"),
    path('success/', views.success, name="succes"),
    path('', views.home_inventaire),
    path('pole/', views.show_pole),
    path('categorie/<str:categorie>', views.show_product),
    path('pole/<str:pole_name>',views.show_category),
    # path('ajout_produit/', views.ajout_Produit, name="nouveau_produit"),
    path('login/', views.check_login, name="login_produit")
]
