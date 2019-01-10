from django.shortcuts import render, redirect
from .models import product
from inventaire.forms import ReservationForm

def home(request):
    produit = product.objects.all()

    return render(request, 'inventaire/home-inventaire.html', {'oui':produit})

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
                form.save()
                return redirect('../')
        else:
            product_ref_final = product_ref
        return render(request, 'inventaire/reservation.html', locals())
    return render(request, 'inventaire/home-inventaire.html')