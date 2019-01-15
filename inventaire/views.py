from django.shortcuts import render, redirect
from .models import product, category, pole
from inventaire.forms import ReservationForm

def home_inventaire(request):
    produit = product.objects.all()

    return render(request, 'inventaire/home-inventaire.html', {'oui':produit})

def show_category(request, pole_name):
    poles = pole.objects.filter(pole_Name=pole_name)
    categories = category.objects.filter(pole_id=poles[0])

    return render(request, 'inventaire/category.html', {'cat_list':categories})

def reservation(request):
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
