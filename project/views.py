from django.shortcuts import render, redirect
from inventaire.models import project_List, project_Reservation, product
from django.template.loader import render_to_string
from .forms import *
from django.contrib.auth import authenticate, login
from datetime import date, time, datetime

# Create your views here.


def show_home(request):

    return render(request, 'project/home-project.html')

def reservation_projet_form(request, project_name, first_name):
    project_Name = project_name
    name = first_name
    date = datetime.now()
    form = ReservationProjectForm(request.POST or None)
    if request.method == 'POST':
        new_project_name = project_List.objects.filter(project_Name=project_Name)
        update_reservation = project_Reservation.objects.filter(project_Name=new_project_name[0], first_Name=name)
        if form.is_valid():
            form = form.save(commit=False)
            for object in update_reservation:
                object.first_Name = form.first_Name
                object.last_Name = form.last_Name
                object.promotion = form.promotion
                object.starting_Date = date.date()
                object.save()
        id_success = 6
        id_button = "/projet"
        return render(request, 'success.html', {'id_success': id_success, 'id_button':id_button})
    else:
        return render(request, 'project/reservation_projet_form.html', locals(), {project_name, first_name})


def reservation_projet(request, project_name):
    queryset_pl = project_List.objects.get(project_Name=project_name)
    project = project_Reservation.objects.filter(project_Name_id = queryset_pl.id)
    return render(request, 'project/reservation_projet.html', {'project': project})

def promotion_project(request, promotion):

    promotion_project_list = project_List.objects.filter(promotion='A'+str(promotion))
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

def check_login_launch_project(request, project_name, promotion):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('launch_project', project_name, promotion)
        else:
            id_error = 5
            return render(request, 'error.html', {'id_error': id_error})
    else:
        form = loginForm(request.POST or None)
        return render(request,'project/login_launch.html', locals(), {project_name, promotion})

def new_project(request):
    form = AjoutProjetForm(request.POST or None)
    form2 = AjoutProjetMatForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            name_Project = form.project_Name
            form.save()
            queryset = project_List.objects.filter(project_Name=name_Project)
            form2 = form2.save(commit=False)
            form2.project_Name = queryset[0]
            form2.save()
            id_success = 3
            id_button = "/projet"
            return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
    return render (request, 'project/nouveau_projet.html', locals())

def launch_project(request, project_name, promotion):
    project_Name = project_name
    promo = promotion
    form = LaunchProjectForm(request.POST or None)
    if request.method == 'POST':
        nb_project = request.POST.get('nb_project')
        nb_project = int(nb_project)
        if nb_project <= 0:
            id_error = 6
            return render(request, 'error.html', {'id_error': id_error})
        else:
            for i in range (1, (nb_project+1)):
                new_reservation = project_Reservation()
                new_project_name = project_List.objects.filter(project_Name=project_Name)
                new_reservation.first_Name = i
                new_reservation.project_Name = new_project_name[0]
                new_reservation.promotion = 'A' + str(promo)
                new_reservation.save()
            id_success = 5
            id_button = "/projet"
            return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
    else:
        return render(request, 'project/lancer_projet.html', locals(), {project_name, promotion})