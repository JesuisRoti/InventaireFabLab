from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('projet/', views.show_home),
    path('projet/<int:promotion>', views.promotion_project, ),
    path('new_project/', views.new_project, name="new_project"),
    path('login/', views.check_login, name="login_projet"),
    re_path(r'^launch_project/(?P<project_name>.+)/(?P<promotion>[1-5])', views.launch_project, name="launch_project"),
    re_path(r'^login_launch/(?P<project_name>.+)/(?P<promotion>[1-5])', views.check_login_launch_project, name="login_launch"),
    re_path('reservation_projet/(?P<project_name>.+)', views.reservation_projet, name="reservation_projet"),
    re_path('reservation_projet_form/(?P<project_name>.+)/(?P<first_name>.+)', views.reservation_projet_form, name="reservation_projet_form"),
    re_path(r'^login_supprimer/(?P<project_name>.+)/(?P<first_name>.+)', views.check_login_supprimer,
            name="login_supprimer"),
    path('supprimer_project_reservation/<str:project_Name>/<str:project_First_Name>', views.supprimer_project_reservation, name="supprimer_project_reservation"),
]