from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('reservation/', views.reservation, name="reservation")
    # path('categorie/<str:categorie>', views.voir_categorie),
]
