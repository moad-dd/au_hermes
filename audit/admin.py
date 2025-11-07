from django.contrib import admin
from .models import Historique


@admin.register(Historique)
class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ('fonctionnaire', 'type_action', 'date_action', 'user')
    list_filter = ('type_action', 'date_action')
    search_fields = ('fonctionnaire__nom', 'fonctionnaire__prenom', 'type_action', 'details')
    ordering = ('-date_action',)
