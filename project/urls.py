from django.urls import path, include
from . import views

urlpatterns = [
    path('projet/', views.show_home),
    path('projet/<int:promotion>', views.promotion_project, ),
    path('new_project/', views.new_project, name="new_project"),
    path('login/', views.check_login, name="login_projet"),
]