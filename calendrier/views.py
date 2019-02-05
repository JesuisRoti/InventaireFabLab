from django.shortcuts import render, redirect
from inventaire.models import *
from django.template.loader import render_to_string
from inventaire.forms import *
from django.contrib.auth import authenticate, login
from django.views.generic.dates import WeekArchiveView
import datetime
from django.contrib.postgres.search import SearchVector

def show_home_calendrier(request):
    # Vue pour montrer les retours prévus dans les 6 prochains jours
    i=0
    j = 0
    n = 6
    p = 3
    # Déclaration de compteurs et de variables pour la matrice
    date_today = test_date(-1)
    date_list = [[[0 for t in range(p)] for u in range(p)] for g in range(n)]
    # Déclaration d'un tableau à 3 dimensions
    while j < 6:
        date_list[j][i] = test_date(j)
        j+=1
    # On remplit la première partie du tableau par les dates de la semaine a venir
    i = 0
    j = 0
    while i < 6:
        date_jour = date_list[i][0]
        queryset = reservation.objects.filter(return_Date=date_jour)
        # Recherche des reservations se terminant le jour compris dans le tableau
        queryset_project = project_reservation_material.objects.filter(return_Date=date_jour)
        # Recherche des project_reservations se terminant le jour compris dans le tableau

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
    #     Pour les réservations et les project_reservations même principe, on récupère l'id du produit pour obtenir son
    #     instance dans la table product. On rajoute ensuite le nom du produit et la quantité dans la query et ensuite
    #     dans la troisième partie du tableau
    return render(request, 'calendrier/home.html', {'date_today':date_today, 'date_list':date_list})

def test_date(i):
    # calcule la date du jour + le nombre de jours qu'on lui transmet
    date_today = datetime.date.today() + datetime.timedelta(days=i+1)
    return (date_today)

def show_daily(request):
    # Vue pour les réservations en cas de clic sur une des journées
    date = request.POST.get('date_jour')
    # récupération de la date
    queryset = reservation.objects.filter(return_Date = date)
    queryset_project = project_reservation_material.objects.filter(return_Date = date)
    # Query sur les tables reserrvations et project_reservations grâce à la date
    for query in queryset:
        produit_objet = query.id_Product
        produit_name = product.objects.get(id=produit_objet)
        query.product_Name = produit_name.product_Name
        # On récupère l'id du produit, on utilise cet id pour chercher le nom du produit dans la table product
        # On rajoute le nom du produit dans la query
    for query_project in queryset_project:
        produit_objet = query_project.id_Product
        reservation_objet = project_Reservation.objects.get(id=query_project.id_Project_Reservation)
        produit_name = product.objects.get(id=produit_objet)
        query_project.product_Name = produit_name.product_Name
        query_project.reservation = reservation_objet
    return render(request, 'calendrier/daily.html', {'reservations':queryset, 'project_reservation':queryset_project}, locals())

def show_historique(request):
    # Vue pour afficher l'historique complet des réservations
    reservations = reservation.objects.all().order_by('-starting_Date')
    reservations_project = project_reservation_material.objects.all().order_by('-id')

    for res in reservations_project:
        projet_objet = project_Reservation.objects.get(id= res.id_Project_Reservation)
        res.first_Name = projet_objet.first_Name
        res.last_Name = projet_objet.last_Name
        res.starting_Date = projet_objet.starting_Date
        res.promotion = projet_objet.promotion
        res.project_Name = projet_objet.project_Name

    # Query sur la table project_reservations et copie des informations récupérés dans la query reservations_project

    return render(request, 'calendrier/historique.html', {'reservations':reservations, 'project_reservations':reservations_project})

def rechercher_produit(request):

    recherche = request.POST.get('recherche')
    global compteur, emprunte, rendu
    compteur, emprunte, rendu = 0, 0, 0
    # Déclaration de compteus globaux

    if len(recherche) >= 3 :
        produits = product.objects.filter(product_Name__contains=recherche)
        for produit in produits:
            resa = reservation.objects.filter(id_Product=produit)
            for nonnull in resa:
                emprunte += nonnull.quantity
                if nonnull.return_Quantity != None:
                    compteur += nonnull.quantity - nonnull.return_Quantity
                    rendu += nonnull.return_Quantity
        #     Query pour un produit sur la table reservation. Si l'objet n'est pas rendu on incrémente les compteurs
        if produits:
            return render (request, 'calendrier/test.html', {'produits':produits, 'reservations':resa, 'taille':len(produits), 'compteur':compteur, 'rendu':rendu, 'emprunte':emprunte})
        else:
            id_error = 8
            return render (request, 'error.html', {'id_error':id_error, 'recherche':recherche})
    else:
        id_error = 9
        return render (request, 'error.html', {'id_error':id_error, 'recherche':recherche})

def show_resa(request, nom_Produit):
    global casse, emprunte, rendu
    casse, emprunte, rendu = 0, 0, 0
    produit_objet = product.objects.filter(product_Name = nom_Produit)
    # récupération du nom du produit recherché, on effectue une query sur la table product pour récupérer l'instance de celui ci
    for produit in produit_objet:
        resa = reservation.objects.filter(id_Product=produit)
        #     Query pour un produit sur la table reservation. Si l'objet n'est pas rendu on incrémente les compteurs
        for nonnull in resa:
            emprunte += nonnull.quantity
            if nonnull.return_Quantity != None:
                rendu += nonnull.return_Quantity
                casse += nonnull.quantity - nonnull.return_Quantity

    return render(request, 'calendrier/test.html', {'produits':produit_objet, 'reservations':resa, 'taille':1, 'compteur':casse, 'rendu':rendu, 'emprunte':emprunte})

def show_resa_en_cours(request):
    reservations = reservation.objects.filter(return_Quantity=None).order_by('-starting_Date')
    for reservat in reservations:
        if reservat.return_Date != None:
            if reservat.return_Date < datetime.date.today():
                reservat.attention = "retard"
    #             En cas de retard on affiche une alerte retard
    reservations_project = project_reservation_material.objects.filter(return_Quantity=None).order_by('-id')

    for res in reservations_project:
        projet_objet = project_Reservation.objects.get(id= res.id_Project_Reservation)
        res.first_Name = projet_objet.first_Name
        res.last_Name = projet_objet.last_Name
        res.starting_Date = projet_objet.starting_Date
        res.promotion = projet_objet.promotion
        res.project_Name = projet_objet.project_Name
    # Query sur la table project_reservations et copie des informations récupérées dans la query reservations_project

    return render (request, 'calendrier/historique.html', {'reservations':reservations, 'project_reservations':reservations_project})