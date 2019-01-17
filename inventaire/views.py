from django.shortcuts import render, redirect
from .models import product, reservation, category, pole
from inventaire.forms import *
from datetime import date, time, datetime
from django.contrib.auth import authenticate, login

def home(request):
    produit = product.objects.all()

    return render(request, 'inventaire/home.html', {'oui':produit})

def error(request):
    return render(request, '/error.html')

def success(request):
    return render(request, '/error.html')

def show_category(request, pole_name):
    poles = pole.objects.filter(pole_Name=pole_name)
    categories = category.objects.filter(pole_id=poles[0])

    return render(request, 'inventaire/category.html', {'cat_list': categories, 'pole_name': pole_name})

def reserver(request):
    if request.method == 'POST':
        global product_ref_final
        product_ref = request.POST.get('product_Ref')
        form = ReservationForm(request.POST or None)
        if not (product_ref):
            if form.is_valid():
                form = form.save(commit=False)
                produit = product.objects.filter(product_Ref=product_ref_final)
                for produit in produit:
                    form.id_Product = produit
                    if (produit.available_Product >= form.quantity):
                        produit.available_Product += -form.quantity
                        produit.save()
                    else:
                        id_error = 1
                        return render(request, 'error.html', {'id_error': id_error})
                form.save()
                id_success = 1
                id_button = "/pole"
                return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
        else:
            product_ref_final = product_ref
        return render(request, 'inventaire/reservation.html', locals())
    return render(request, 'inventaire/home.html')

def  show_product(request, categorie):
    id_category = category.objects.filter(category_name=categorie)
    categories = product.objects.filter(id_Category=id_category[0])
    print(categorie)

    return render(request, 'inventaire/category.html', {'cat_products':categories, 'category_name':categorie})

def show_pole(request):
    poles = pole.objects.all()

    return render(request, 'inventaire/category.html', {'poles_list':poles})


def retour(request):
    global product_ref_final
    form = RetourForm(request.POST or None)
    date = datetime.now()
    if request.method == 'POST':
        product_ref = request.POST.get('product_Ref')
        if not (product_ref):
            if form.is_valid():
                form = form.save(commit=False)
                produit = product.objects.filter(product_Ref=product_ref_final)
                retour = reservation.objects.filter(id_Product=produit[0],
                                                 first_Name= form.first_Name,
                                                 last_Name=form.last_Name,
                                                 promotion=form.promotion,
                                                 return_Quantity=None)
                if not retour:
                    id_error = 2
                    return render(request, 'error.html', {'id_error': id_error})
                elif form.return_Quantity > retour[0].quantity:
                    id_error = 3
                    return render(request, 'error.html', {'id_error': id_error})
                else:
                    for retour in retour:
                        retour.return_Date = date.date()
                        retour.save(update_fields=['return_Date'])
                        retour.return_Quantity = form.return_Quantity
                        retour.save(update_fields=['return_Quantity'])
                        for produit in produit:
                            produit.available_Product += form.return_Quantity
                            produit.save(update_fields=['available_Product'])
                    id_success = 2
                    id_button = "/pole"
                    return render(request, 'success.html', {'id_success': id_success, 'id_button':id_button})
        else:
            product_ref_final = product_ref
        return render(request, 'inventaire/retour.html', locals())
    return render(request, 'inventaire/home.html')

def check_login(request, cat_name):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('nouveau_produit', cat_name)
        else:
            id_error = 5
            return render(request, 'error.html', {'id_error': id_error})
    else:
        form = loginForm(request.POST or None)
        return render(request,'inventaire/formulaire/login.html', locals(), cat_name)


def ajout_Produit(request, cat_name):
    global categorie_name_final
    categorie_name = cat_name
    form = NouveauProduitForm(request.POST or None)
    form2 = ModificationStockForm(request.POST or None)
    if request.method == 'POST':
        print (categorie_name_final)
        categorie_objet = category.objects.filter(category_name=categorie_name_final)
        if form.is_valid() and form2.is_valid():
            form = form.save(commit=False)
            form2 = form2.save(commit=False)
            if form.available_Product <= form.stock:
                form.id_Category = categorie_objet[0]
                categorie_ref = categorie_objet[0].category_Ref
                pole_id = categorie_objet[0].pole_id
                pole_object = pole.objects.filter(pole_Name=pole_id.pole_Name)
                pole_ref = pole_object[0].pole_Ref
                product_len = product.objects.count() + 1
                product_ref = pole_ref + categorie_ref + str(product_len)
                form2.name_Product = form.product_Name
                form.product_Ref = product_ref
                form2.modification = "ajout"
                form.save()
                form2.save()
                id_success = 4
                id_button = "/pole"
                return render(request, 'success.html', {'id_success': id_success, 'id_button': id_button})
            else:
                id_error = 4
                return render(request, 'error.html', {'id_error': id_error})
    else:
        categorie_name_final = categorie_name
        return render(request, 'inventaire/formulaire/nouveau_produit.html', locals(), cat_name)
    cat_name = local
    return render(request, 'inventaire/formulaire/nouveau_produit.html', locals(), cat_name)


# def check_login(request):
#     if request.method == 'POST':
#         global mdp, nomdecompte, cat_name_final, i
#         mdp = request.POST.get('mdp')
#         nomdecompte = request.POST.get('nomdecompte')
#         cat_name = request.POST.get('cat_name')
#         user = authenticate(request, username=nomdecompte, password=mdp)
#
#         if user is not None:
#             login(request, user)
#             form1 = NouveauProduitForm(request.POST or None)
#             form2 = ModificationStockForm(request.POST or None)
#             if not cat_name:
#                 if form1.is_valid():
#                     print ('oui')
#                 if form2.is_valid():
#                     print ('form2')
#                 categorie_objet = category.objects.filter(category_name=cat_name_final)
#                 categorie_ref = categorie_objet[0].category_Ref
#                 pole_id = categorie_objet[0].pole_id
#                 pole_object = pole.objects.filter(pole_Name=pole_id.pole_Name)
#                 pole_ref = pole_object[0].pole_Ref
#                 product_len = product.objects.count() + 1
#                 product_ref = pole_ref + categorie_ref + str(product_len)
#                 print ('ebug4')
#                 if form1.is_valid() and form2.is_valid():
#                     form1 = form1.save(commit=False)
#                     form2 = form2.save(commit=False)
#                     print ('ebug3')
#                     if form1.available_Product <= form1.stock:
#                         form1.id_Category = categorie_objet[0]
#                         form2.name_Product = form1.product_Name
#                         form2.modification = "ajout"
#                         print ('ebug2')
#
#                         # form1.save()
#                         # form2.save()
#                         return redirect('../')
#                     else:
#                         id_error = 6
#                         return redirect('error.html', {'id_error': id_error})
#         else:
#             cat_name_final = cat_name
#             print('oui'+user)
#             form1 = loginForm(request.POST or None)
#             return render(request, 'inventaire/formulaire/login.html', locals())
#
#         print ('cat_name_final :' + cat_name_final)
#         return render(request,'inventaire/formulaire/login.html', locals())
#     else:
#         print('else')
#         form = loginForm(request.POST or None)
#         return render(request,'inventaire/formulaire/login.html', locals())

