from django import forms
from inventaire.models import *
from django.forms.widgets import HiddenInput
from django.forms import formset_factory


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

class ConfForm(forms.Form):
    """
    Formulaire de configuration du module
    """
    format_x = forms.IntegerField(label="Largeur", required=True, min_value=0, widget=forms.TextInput(
        attrs={'placeholder': 'mm', 'class': 'form-control input-sm'}))
    format_y = forms.IntegerField(label="Hauteur", required=True, min_value=0, widget=forms.TextInput(
        attrs={'placeholder': 'mm', 'class': 'form-control input-sm'}))

class SorteForm(forms.Form):

    #Champs multiples
    designation = forms.CharField( label="Désignation", required=True, widget=forms.TextInput(attrs={'placeholder':'','class':'form-control input-sm'}) )
    quantite = forms.IntegerField( label="Quantité", required=True, min_value=0, widget=forms.TextInput(attrs={'placeholder':'','class':'form-control input-sm'}) )
    rectoverso = forms.ChoiceField(label='',choices = [(False,'Recto Seul'),(True,'Recto Verso')],required=True,widget=forms.Select( attrs={'class':'form-control input-sm'}))