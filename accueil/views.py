from django.shortcuts import render, redirect
from inventaire.models import *
from django.template.loader import render_to_string
from inventaire.forms import *
from django.contrib.auth import authenticate, login

def show_home(request):
    # Vue servant à affiher la page d'accueil

    article_securite = security_article.objects.order_by('date')
    article_profession = profession_article.objects.order_by('date')
    article_news = news_article.objects.order_by('date')
    # Queryset pour récupérer les différents articles danns la table

    return render(request, 'accueil/accueil.html', {'securite':article_securite,
                                                    'metier':article_profession,
                                                    'actualite':article_news,})
    # Envoi des différents articles au template "accueil.html"

def lire(request, id, cat):
    # Vue pour lire un article en entier
    if cat=="secu":
        fiche = security_article.objects.get(id=id)
    if cat == "metier":
        fiche = profession_article.objects.get(id=id)
    if cat == "actu":
        fiche = news_article.objects.get(id=id)
    if not cat:
        return render (request, 'error.html')
    # On récupère la catégorie et l'id de l'article pour savoir dans quelle table chercher l'article
    return render (request, 'accueil/lire.html', {'fiche':fiche})

    # On envoie le bon article au template "lire.html"