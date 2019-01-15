from django import forms
from inventaire.models import *
from django.forms.widgets import HiddenInput

class AjoutProjetForm (forms.ModelForm):
    class Meta:
        model = project_List
        fields = '__all__'

class loginForm(forms.Form):
    nomdecompte = forms.CharField(max_length=100, label="Nom de compte")
    mdp = forms.CharField(widget=forms.PasswordInput, max_length=100, label = "Mot de passe")