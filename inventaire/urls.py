from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_inventaire),
    path('reservation/', views.reservation, name="reservation"),
    path('pole/', views.show_pole),
    path('categorie/<str:categorie>', views.show_product),
    path('pole/<str:pole_name>',views.show_category)
]
