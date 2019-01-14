from django import forms
from .models import reservation
from django.forms.widgets import HiddenInput

class ReservationForm (forms.ModelForm):
    class Meta:
        model = reservation
        widgets = {'id_Product': forms.HiddenInput()}
        exclude = ('return_Quantity',)
