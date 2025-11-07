from django import forms
from .models import Fonctionnaire, Employee


class FonctionnaireForm(forms.ModelForm):
    class Meta:
        model = Fonctionnaire
        fields = ['ss', 'nom', 'prenom', 'grade', 'date_rec', 'statut', 'telephone', 'photo']
        widgets = {
            'date_rec': forms.DateInput(attrs={'type': 'date'}),
        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['position', 'department', 'base_salary', 'bonus', 'deductions', 'date_hired']
        widgets = {
            'date_hired': forms.DateInput(attrs={'type': 'date'}),
        }