from django.shortcuts import render, redirect
from inventaire.models import *
from django.template.loader import render_to_string
from inventaire.forms import *
from django.contrib.auth import authenticate, login

def show_home(request):

    article_securite = security_article.objects.order_by('date')
    article_profession = profession_article.objects.order_by('date')
    article_news = news_article.objects.order_by('date')

    return render(request, 'accueil/accueil.html', {'securite':article_securite,
                                                    'metier':article_profession,
                                                    'actualite':article_news})

def lire(request, id, cat):
    if cat=="secu":
        fiche = security_article.objects.get(id=id)
    if cat == "metier":
        fiche = profession_article.objects.get(id=id)
    if cat == "actu":
        fiche = news_article.objects.get(id=id)
    if not cat:
        return render (request, 'error.html')

    return render (request, 'accueil/lire.html', {'fiche':fiche})