from django.shortcuts import render, redirect

# Create your views here.


def show_home(request):

    return render(request, 'projet/home-projet.html')

