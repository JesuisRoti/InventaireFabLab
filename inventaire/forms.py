from django import forms
from .models import reservation
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