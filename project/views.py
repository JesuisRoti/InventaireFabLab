from django.shortcuts import render, redirect
from inventaire.models import project_List
from django.template.loader import render_to_string

# Create your views here.


def show_home(request):

    return render(request, 'project/home-project.html')

def promotion_project(request, promotion):

    promotion_project_list = project_List.objects.filter(promotion='A'+str(promotion))
    print(promotion_project_list)
    return render(request, 'project/promotion-project', {'promotion': promotion,
                                                         'promotion_project_list': promotion_project_list})
