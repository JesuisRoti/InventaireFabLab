from django.shortcuts import render, redirect
from inventaire.models import *
from django.template.loader import render_to_string
from inventaire.forms import *
from django.contrib.auth import authenticate, login
from django.views.generic.dates import WeekArchiveView
import datetime

def show_home_calendrier(request):
    i=0
    j = 0
    n = 6
    p = 3
    date_today = test_date(-1)
    date_list = [[[0 for t in range(p)] for u in range(p)] for g in range(n)]
    # distance = [[[0 for k in xrange(n)] for j in xrange(n)] for i in xrange(n)]
    # date = date_today + datetime.timedelta(days=7)
    # queryset_resa = reservation.objects.filter(return_Date__gt = date_today)
    # q = queryset_resa.exclude(return_Date__gt=date)
    while j < 6:
        date_list[j][i] = test_date(j)
        j+=1
    print (date_list)
    i = 0
    j = 0
    while i < 6:
        date_jour = date_list[i][0]
        queryset = reservation.objects.filter(return_Date=date_jour)
        queryset_project = project_reservation_material.objects.filter(return_Date=date_jour)
        for query in queryset:
            if j<3:
                produit_objet = query.id_Product
                produit_name = product.objects.get(id=produit_objet)
                query.product_Name = produit_name.product_Name
                quantite = str(query.quantity)
                date_list[i][1][j] = query.product_Name + ' X ' + quantite
                j+=1
        j = 0
        for query_project in queryset_project:
            if j<3:
                produit_objet = query_project.id_Product
                produit_name = product.objects.get(id=produit_objet)
                query_project.product_Name = produit_name.product_Name
                quantite = str(query_project.quantity)
                date_list[i][2][j] = query_project.product_Name + ' X ' + quantite
                j +=1
        j = 0
        i+=1
    return render(request, 'calendrier/home.html', {'date_today':date_today, 'date_list':date_list})

def test_date(i):
    # calcule la date du jour + le nombre de jours qu'on lui transmet
    date_today = datetime.date.today() + datetime.timedelta(days=i+1)
    return (date_today)

def show_daily(request):
    date = request.POST.get('date_jour')
    produit_queryset = []
    print (date)
    queryset = reservation.objects.filter(return_Date = date)
    queryset_project = project_reservation_material.objects.filter(return_Date = date)
    for query in queryset:
        produit_objet = query.id_Product
        produit_name = product.objects.get(id=produit_objet)
        query.product_Name = produit_name.product_Name
        print(query.product_Name)
    for query_project in queryset_project:
        produit_objet = query_project.id_Product
        reservation_objet = project_Reservation.objects.get(id=query_project.id_Project_Reservation)
        produit_name = product.objects.get(id=produit_objet)
        query_project.product_Name = produit_name.product_Name
        query_project.reservation = reservation_objet
    return render(request, 'calendrier/dayli.html', {'reservations':queryset, 'project_reservation':queryset_project}, locals())

def show_historique(request):
    reservations = reservation.objects.all()
    reservations_project = project_reservation_material.objects.all()

    for res in reservations_project:
        projet_objet = project_Reservation.objects.get(id= res.id_Project_Reservation)
        res.first_Name = projet_objet.first_Name
        res.last_Name = projet_objet.last_Name
        res.starting_Date = projet_objet.starting_Date
        res.promotion = projet_objet.promotion
        res.project_Name = projet_objet.project_Name

    return render(request, 'calendrier/historique.html', {'reservations':reservations, 'project_reservations':reservations_project})