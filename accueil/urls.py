from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.show_home),
    path('home/', views.show_home),
    path('article/<int:id><str:cat>', views.lire, name='lire')
]