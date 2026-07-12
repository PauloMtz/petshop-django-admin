from django import forms
from ..models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'nascimento', 'categoria', 'cor']
        # o dono vai como parâmetro da rota
        exclude = ['dono', ]

