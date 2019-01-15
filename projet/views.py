from django.shortcuts import render, redirect
from projet.forms import *
from django.contrib.auth import authenticate, login
# Create your views here.


def show_home(request):

    return render(request, 'projet/home-projet.html')

def check_login(request):
    if request.method == 'POST':
        global mdp, nomdecompte
        mdp = request.POST.get('mdp')
        nomdecompte = request.POST.get('nomdecompte')
        user = authenticate(request, username=nomdecompte, password=mdp)

        if user is not None:
            login(request, user)
            return redirect('new_project')
    else:
        form = loginForm(request.POST or None)
        return render(request,'projet/login.html', locals())

def new_project(request):
    form = AjoutProjetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../projet')
    return render (request, 'projet/nouveau_projet.html', locals())