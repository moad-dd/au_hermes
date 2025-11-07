from django.contrib import admin
from .models import Fonctionnaire, Employee


@admin.register(Fonctionnaire)
class FonctionnaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'ss', 'grade', 'statut', 'date_rec')
    list_filter = ('statut', 'grade')
    search_fields = ('nom', 'prenom', 'ss')
    ordering = ('-date_rec',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'department', 'base_salary', 'date_hired')
    list_filter = ('department',)
    search_fields = ('user__username', 'position', 'department')
    ordering = ('-date_hired',)
