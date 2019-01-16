from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation/', views.reserver, name="reservation"),
    path('retour/', views.retour, name="retour"),
    path('error/', views.error, name="erreur"),
    path('success/', views.success, name="succes"),
    path('', views.home),
    path('pole/', views.show_pole),
    path('categorie/<str:categorie>', views.show_product),
    path('pole/<str:pole_name>',views.show_category)
]
