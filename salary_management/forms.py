from django import forms
from .models import Paie, Prime


class PaieForm(forms.ModelForm):
    class Meta:
        model = Paie
        fields = ['mois', 'annee', 'salaire_base', 'indemnites', 'retenues', 'net_a_payer']


class PrimeForm(forms.ModelForm):
    class Meta:
        model = Prime
        fields = ['type_prime', 'montant', 'date_prime', 'description']
        widgets = {
            'date_prime': forms.DateInput(attrs={'type': 'date'}),
        }