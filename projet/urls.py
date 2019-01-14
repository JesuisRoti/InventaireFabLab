from django.urls import path, include
from . import views

urlpatterns = [
    path('projet/', views.show_home)
]