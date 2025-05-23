from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'weight', 'height', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Charmander'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fuego'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id' : 'image_field',
            }),
        }