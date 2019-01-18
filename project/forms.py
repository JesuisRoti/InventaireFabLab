from django import forms
from inventaire.models import *
from django.forms.widgets import HiddenInput
from dal import autocomplete


class AjoutProjetForm (forms.ModelForm):
    class Meta:
        model = project_List
        fields = '__all__'


class AjoutProjetMatForm(forms.ModelForm):
    class Meta:
        model = project_material
        exclude = ('project_Name',)
        widget = {
            'id_Product': autocomplete.ModelSelect2(
                url='select2_fk'
            )
        }

        # id_Product = forms.ModelChoiceField(
        #     queryset=product.objects.all(),
        #     widget=autocomplete.ModelSelect2(url='test-autocomplete')
        # )


class loginForm(forms.Form):
    nomdecompte = forms.CharField(max_length=100, label="Nom de compte")
    mdp = forms.CharField(widget=forms.PasswordInput, max_length=100, label = "Mot de passe")