from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    # path('categorie/<str:categorie>', views.voir_categorie),
]
