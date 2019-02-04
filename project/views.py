from django.shortcuts import render, redirect
from inventaire.models import project_List, project_Reservation, product, project_material
from django.template.loader import render_to_string
from .forms import *
from django.contrib.auth import authenticate, login
from datetime import date, time, datetime, timedelta
from django.forms import formset_factory
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
            print (new_project_name[0].duration)
            for object in update_reservation:
                object.first_Name = form.first_Name
                object.last_Name = form.last_Name
                object.promotion = form.promotion
                object.starting_Date = date.date()
                object.return_Date = date.date() + timedelta(days=new_project_name[0].duration)
                object.save()
        #         update de la table project_reservation_material
                update_project_reservation_material = project_reservation_material.objects.filter(id_Project_Reservation = object)
                for update_project_reservation_material in update_project_reservation_material:
                    update_project_reservation_material.return_Date = object.return_Date
                    update_project_reservation_material.save()

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
    return render(request, 'project/promotion-project.html', {'promotion': promotion,
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
    AjoutProjetMatFormSet = formset_factory(AjoutProjetMatForm)
    form2 = AjoutProjetMatFormSet(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            name_Project = form.project_Name
            form.save()
            queryset = project_List.objects.filter(project_Name=name_Project)
            for simpleform in form2:
                if simpleform.is_valid():
                    simpleform = simpleform.save(commit=False)
                    simpleform.project_Name = queryset[0]
                    simpleform.save()
            id_success = 3
            id_button = "/projet"
            return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
    return render(request, 'project/nouveau_projet.html', locals())

def launch_project(request, project_name, promotion):
    project_Name = project_name
    promo = promotion
    form = LaunchProjectForm(request.POST or None)
    project_Name_List = project_List.objects.filter(project_Name=project_Name)
    products_project = project_material.objects.filter(project_Name=project_Name_List[0])

    if request.method == 'POST':
        nb_project = request.POST.get('nb_project')
        nb_project = int(nb_project)
        if nb_project <= 0:
            id_error = 6
            return render(request, 'error.html', {'id_error': id_error})
        else:

            for product_project in products_project:
                product_Name = product.objects.filter(product_Name = product_project.id_Product)
                product_available = product_Name[0].available_Product
                product_needed = product_project.quantity
                product_needed = int(product_needed)
                if (product_needed * nb_project) > product_available:
                    id_error = 7
                    return render(request, 'error.html', {'id_error': id_error, 'product_Name': product_Name[0].product_Name})

            for product_project in products_project:
                product_Name = product.objects.filter(product_Name = product_project.id_Product)
                product_needed = product_project.quantity
                product_needed = int(product_needed)
                for product_Name in product_Name:
                    product_Name.available_Product += -(product_needed * nb_project)
                    product_Name.save()

            for i in range (1, (nb_project+1)):
                # remplissage de la table reservation_projet avec autant d'entrées que de groupe
                new_reservation = project_Reservation()
                new_project_name = project_List.objects.filter(project_Name=project_Name)
                new_reservation.first_Name = i
                new_reservation.project_Name = new_project_name[0]
                new_reservation.promotion = 'A' + str(promo)
                new_reservation.save()
                # remplissage de la table project_reservation_material avec, nombre de groupe * nombre de produit par projet, entrée
                for product_project in products_project:
                    new_project_reservation_material = project_reservation_material()
                    new_project_reservation_material.id_Project_Reservation = new_reservation
                    new_project_reservation_material.id_Product = product_project.id_Product
                    new_project_reservation_material.quantity = product_project.quantity
                    new_project_reservation_material.save()



            id_success = 5
            id_button = "/projet"
            return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
    else:
        return render(request, 'project/lancer_projet.html', locals(), {project_name, promotion})

def supprimer_project_reservation(request, project_Name, project_First_Name):

    projet_objet = project_List.objects.get(project_Name=project_Name)
    projet_reservation_objet  = project_Reservation.objects.get(first_Name=project_First_Name, project_Name=projet_objet)
    project_reservation_material_objet = project_reservation_material.objects.filter(id_Project_Reservation=projet_reservation_objet)
    for item in project_reservation_material_objet:
        item.delete()
    projet_reservation_objet.delete()

    id_success = 7
    id_button = "/projet"
    return render(request, 'success.html', {'id_success':id_success, 'id_button':id_button})

def check_login_supprimer(request, project_name, first_name):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('supprimer_project_reservation', project_name, first_name)
        else:
            id_error = 5
            return render(request, 'error.html', {'id_error': id_error})
    else:
        form = loginForm(request.POST or None)
        return render(request,'project/login_supprimer.html', locals(), {project_name, first_name})

def rendre_project_reservation(request, project_name, first_name):
    project_object = project_List.objects.get(project_Name=project_name)
    project_reservation = project_Reservation.objects.get(project_Name=project_object, first_Name=first_name)
    project_resa_mat = project_reservation_material.objects.filter(id_Project_Reservation=project_reservation)

    if request.method == 'POST':
        for item in project_resa_mat:
            return_Quantity = int(request.POST.get(str(item.id_Product)))
            if return_Quantity <= 0:
                id_error = 10
                return render(request, 'error.html', {'id_error': id_error})
            elif return_Quantity > item.quantity:
                id_error = 3
                return render(request, 'error.html', {'id_error': id_error})
        for item in project_resa_mat:
            return_Quantity = int(request.POST.get(str(item.id_Product)))
            item.return_Quantity = return_Quantity
            item.save()

            product_Name = product.objects.get(product_Name=item.id_Product)
            print(product_Name.available_Product)
            product_Name.available_Product += return_Quantity
            product_Name.save()
            print(product_Name.available_Product)

        id_success = 8
        id_button = "/projet"
        return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})

    return render(request, 'project/rendre_project_reservation.html', locals(), {project_name, first_name})

def check_login_rendre(request, project_name, first_name):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('retour_Project', project_name, first_name)
        else:
            id_error = 5
            return render(request, 'error.html', {'id_error': id_error})
    else:
        form = loginForm(request.POST or None)
        return render(request,'project/login_rendre.html', locals(), {project_name, first_name})