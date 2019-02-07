from django import forms
from inventaire.models import *
from django.forms.widgets import HiddenInput

class AjoutFicheSecuForm(forms.ModelForm):
    class Meta:
        model = security_article
        fields = '__all__'

class AjoutFicheMetierForm(forms.ModelForm):
    class Meta:
        model = profession_article
        fields = '__all__'

class AjoutFicheActuForm(forms.ModelForm):
    class Meta:
        model = news_article
        fields = '__all__'


class UploadFileForm(forms.Form):
    title = forms.CharField(label="Titre", max_length=50)
    file = forms.FileField(label="Fichier",)
