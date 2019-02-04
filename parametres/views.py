from django.shortcuts import render, redirect
from inventaire.forms import *
from parametres.forms import *
from inventaire.models import *
from datetime import date, time, datetime
from django.contrib.auth import authenticate, login

def show_parameters(request):

    return render (request, 'parameters/home_params.html')

def check_login(request):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('param')
        else:
            id_error = 5
            return render(request, 'error.html', {'id_error': id_error})
    else:
        form = loginForm(request.POST or None)
        return render(request,'parameters/formulaire/login.html', locals())


def gestion_accueil(request):

    fiches_secu = security_article.objects.all()
    fiches_metier = profession_article.objects.all()
    fiches_actu = news_article.objects.all()

    return render (request, 'parameters/gestion_accueil.html', {'secu': fiches_secu, 'metier': fiches_metier, 'actu': fiches_actu})

def changer_show_it(request):
    if request.method == 'POST':
        cat = request.POST.get('categorie')
        id = request.POST.get('id')
        show_It = request.POST.get('show_it')

        if cat == "secu":
            objet = security_article.objects.get(id=id)
        if cat == "metier":
            objet = profession_article.objects.get(id=id)
        if cat == "news":
            objet = news_article.objects.get(id=id)
        if objet:
            if show_It == 'False':
                objet.show_it = True
                objet.save()
            else:
                objet.show_it = False
                objet.save()
    return redirect ('gest_acc')

def choix_type(request):

    return render (request, 'parameters/formulaire/choix_type.html')

def ajouter_fiche(request, categorie):
    if categorie == "secu":
        Form = AjoutFicheSecuForm(request.POST or None)
    if categorie == "metier":
        Form = AjoutFicheMetierForm(request.POST or None)
    if categorie == "actu":
        Form = AjoutFicheActuForm(request.POST or None)
    if request.method == 'POST':
        if Form.is_valid():
            Form.save()
            return render(request, 'success.html')
    else:
        return render (request, 'parameters/formulaire/nouvelle_fiche.html', locals())