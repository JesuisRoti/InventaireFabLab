from django.shortcuts import render, redirect
from inventaire.models import project_List
from django.template.loader import render_to_string
from .forms import *
from django.contrib.auth import authenticate, login


# Create your views here.


def show_home(request):

    return render(request, 'project/home-project.html')

def promotion_project(request, promotion):

    promotion_project_list = project_List.objects.filter(promotion='A'+str(promotion))
    print(promotion_project_list)
    return render(request, 'project/promotion-project', {'promotion': promotion,
                                                         'promotion_project_list': promotion_project_list})


def check_login(request):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('new_project')
        else:
            id_error = 5
            return render(request, 'error.html', {'id_error': id_error})
    else:
        form = loginForm(request.POST or None)
        return render(request,'project/login.html', locals())

def new_project(request):
    form = AjoutProjetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            id_success = 3
            id_button = "/projet"
            return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
    return render (request, 'project/nouveau_projet.html', locals())