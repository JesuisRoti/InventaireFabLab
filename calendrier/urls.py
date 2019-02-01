from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('calendrier/', views.show_home_calendrier),
    path('daily/', views.show_daily),
    path('historique', views.show_historique, name='historique'),
    path('rechercher', views.rechercher_produit, name="recherche_Prod"),
    path('produit_recherche/<str:nom_Produit>', views.show_resa)
]