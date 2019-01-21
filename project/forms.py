from django import forms
from inventaire.models import *
from django.forms.widgets import HiddenInput


class AjoutProjetForm (forms.ModelForm):
    class Meta:
        model = project_List
        fields = '__all__'


class AjoutProjetMatForm(forms.ModelForm):
    class Meta:
        model = project_material
        exclude = ('project_Name',)


        # id_Product = forms.ModelChoiceField(
        #     queryset=product.objects.all(),
        #     widget=autocomplete.ModelSelect2(url='test-autocomplete')
        # )


class loginForm(forms.Form):
    nomdecompte = forms.CharField(max_length=100, label="Nom de compte")
    mdp = forms.CharField(widget=forms.PasswordInput, max_length=100, label = "Mot de passe")

class LaunchProjectForm(forms.Form):
    nb_project = forms.IntegerField(label="Nombre de groupe de projet")

class ReservationProjectForm(forms.ModelForm):
    class Meta:
        model = project_Reservation
        # widgets = {'project_Name': forms.HiddenInput()}
        exclude = ('starting_Date', 'return_Date', 'project_Name')