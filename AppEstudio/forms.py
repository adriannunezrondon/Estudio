__author__ = 'adrian'

from django import forms
from AppEstudio.models import Mascota, Persona
from django.contrib.admin import widgets


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',

        ]

        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad Aproximada',
            'fecha_rescate': 'Fecha Rescate yyyy-mm-dd',
            'persona': 'Persona Adoptante',
            'vacuna': 'Vacuna'

        }
        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.DateInput(),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
            ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control'}),
            }


