from django.contrib import admin
from .models import LeaveRequest, Conge


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'leave_type')
    search_fields = ('employee__user__username', 'reason')
    ordering = ('-date_submitted',)


@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ('fonctionnaire', 'type_conge', 'date_debut', 'date_fin')
    list_filter = ('type_conge',)
    search_fields = ('fonctionnaire__nom', 'fonctionnaire__prenom', 'motif')
    ordering = ('-date_debut',)
