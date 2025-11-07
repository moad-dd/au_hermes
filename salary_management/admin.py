from django.contrib import admin
from .models import Paie, Prime


@admin.register(Paie)
class PaieAdmin(admin.ModelAdmin):
    list_display = ('fonctionnaire', 'mois', 'annee', 'salaire_base', 'net_a_payer')
    list_filter = ('annee', 'mois')
    search_fields = ('fonctionnaire__nom', 'fonctionnaire__prenom')
    ordering = ('-annee', '-mois')


@admin.register(Prime)
class PrimeAdmin(admin.ModelAdmin):
    list_display = ('fonctionnaire', 'type_prime', 'montant', 'date_prime')
    list_filter = ('type_prime',)
    search_fields = ('fonctionnaire__nom', 'fonctionnaire__prenom', 'type_prime')
    ordering = ('-date_prime',)
