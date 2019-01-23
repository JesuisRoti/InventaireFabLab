from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('parametres/', views.show_parameters, name='param'),
    path('parametres/login/', views.check_login, name="login_param"),
    path('parametres/GestionAccueil', views.gestion_accueil, name="gest_acc"),
    path('parametres/Change', views.changer_show_it, name="changer_show_it")
    ]
