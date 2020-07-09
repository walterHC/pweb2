from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
                'nombreCiudad',
                'imagenCiudad',
                'descripcionCiudad',
                'precioTour',
                'ofertaTour',
                ]

class RawDestinationForm(forms.Form):
    nombreCiudad = forms.CharField()
    imagenCiudad = forms.ImageField()
    descripcionCiudad = forms.CharField(
                widget= forms.Textarea(
                    attrs={
                        'cols':'10',
                    }
                )
            )
    precioTour = forms.IntegerField()
    ofertaTour = forms.BooleanField()
