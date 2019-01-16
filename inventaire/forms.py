from django import forms
from .models import reservation, product, stock_modification
from django.forms.widgets import HiddenInput

class ReservationForm (forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = reservation
        widgets = {'id_Product': forms.HiddenInput()}
        exclude = ('return_Quantity',)

class RetourForm (forms.ModelForm):
    class Meta:
        model = reservation
        widgets = {'id_Product': forms.HiddenInput(), 'return_Date': forms.HiddenInput()}
        exclude = ('starting_Date', 'quantity',)

class NouveauProduitForm(forms.ModelForm):
    class Meta:
        model = product
        exclude = ('product_Ref', 'id_Category',)

class ModificationStockForm(forms.ModelForm):
    class Meta:
        model = stock_modification
        exclude =('id_Product', 'name_Product', 'modification', )

class loginForm(forms.Form):
    nomdecompte = forms.CharField(max_length=100, label="Nom de compte")
    mdp = forms.CharField(widget=forms.PasswordInput, max_length=100, label = "Mot de passe")