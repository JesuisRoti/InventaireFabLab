from django.shortcuts import render
from .models import Produit

# Create your views here.

def home(request):
    produit = Produit.objects.all()

    return render(request, 'inventaire/home.html', {'oui':produit})

