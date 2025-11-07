from django import forms
from .models import CareerHistory, Promotion, Echelon


class CareerHistoryForm(forms.ModelForm):
    class Meta:
        model = CareerHistory
        fields = ['position_title', 'department', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['date_promotion', 'ancien_grade', 'nouveau_grade', 'observation']
        widgets = {
            'date_promotion': forms.DateInput(attrs={'type': 'date'}),
        }


class EchelonForm(forms.ModelForm):
    class Meta:
        model = Echelon
        fields = ['date_echelon', 'ancien_echelon', 'nouvel_echelon', 'observation']
        widgets = {
            'date_echelon': forms.DateInput(attrs={'type': 'date'}),
        }