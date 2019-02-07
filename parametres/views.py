from django.shortcuts import render, redirect
from inventaire.forms import *
from parametres.forms import *
from inventaire.models import *
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage


def ajouter_image(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(request.POST.get('title'), myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'parameters/formulaire/ajout_image.html', {'form': form,
            'uploaded_file_url': uploaded_file_url
        })
    else:
        form = UploadFileForm(request.POST, request.FILES)
    return render(request, 'parameters/formulaire/ajout_image.html', {'form': form})


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

    # affichage des différentes fiches sur la page de gestion
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
        # on récupère la fiche qui correspond à l'id renseigné
        if objet:
            if show_It == 'False':
                objet.show_it = True
                objet.save()
            else:
                objet.show_it = False
                objet.save()
    #             si show_it est activé on le désactive et vice versa
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
    #     Récupération de la catégorie de la fiche et on affiche un formulaire de création de fiche
    else:
        return render (request, 'parameters/formulaire/nouvelle_fiche.html', locals())