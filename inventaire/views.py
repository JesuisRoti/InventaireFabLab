from django.shortcuts import render, redirect
from .models import product, reservation, category, pole
from inventaire.forms import ReservationForm, RetourForm
from datetime import date, time, datetime

def home_inventaire(request):
    produit = product.objects.all()

    return render(request, 'inventaire/home-inventaire.html', {'oui':produit})

def error(request):
    return render(request, 'inventaire/error.html')

def show_category(request, pole_name):
    poles = pole.objects.filter(pole_Name=pole_name)
    categories = category.objects.filter(pole_id=poles[0])

    return render(request, 'inventaire/category.html', {'cat_list':categories})

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
                        previous_url = request.META.get('HTTP_REFERER')
                        return render(request, 'inventaire/error2.html', {'prev':previous_url})
                form.save()
                return redirect('../')
        else:
            product_ref_final = product_ref
        return render(request, 'inventaire/reservation.html', locals())
    return render(request, 'inventaire/home-inventaire.html')

def  show_product(request, categorie):
    id_category = category.objects.filter(category_name=categorie)
    categories = product.objects.filter(id_Category=id_category[0])
    print(categorie)

    return render(request, 'inventaire/category.html', {'cat_products':categories, 'category_name':categorie})

def show_pole(request):
    poles = pole.objects.all()

    return render(request, 'inventaire/category.html', {'poles_list':poles})


def retour(request):
    if request.method == 'POST':
        global  product_ref_final
        product_ref = request.POST.get('product_Ref')
        form = RetourForm(request.POST or None)
        date = datetime.now()
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
                    id_error = 1
                    return render(request, 'inventaire/error.html', {'id_error': id_error})
                elif form.return_Quantity > retour[0].quantity:
                    id_error = 2
                    return render(request, 'inventaire/error.html', {'id_error': id_error})
                else:
                    for retour in retour:
                        retour.return_Date = date.date()
                        retour.save(update_fields=['return_Date'])
                        retour.return_Quantity = form.return_Quantity
                        retour.save(update_fields=['return_Quantity'])
                        for produit in produit:
                            produit.available_Product += form.return_Quantity
                            produit.save(update_fields=['available_Product'])
                    return redirect('../')
        else:
            product_ref_final = product_ref
        return render(request, 'inventaire/retour.html', locals())
    return render(request, 'inventaire/home-inventaire.html')