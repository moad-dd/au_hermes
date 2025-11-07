from django.contrib import admin
from .models import CareerHistory, Promotion, Echelon


@admin.register(CareerHistory)
class CareerHistoryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'position_title', 'department', 'start_date', 'end_date')
    list_filter = ('department',)
    search_fields = ('employee__user__username', 'position_title', 'department')
    ordering = ('-start_date',)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('fonctionnaire', 'date_promotion', 'ancien_grade', 'nouveau_grade')
    search_fields = ('fonctionnaire__nom', 'fonctionnaire__prenom', 'nouveau_grade')
    ordering = ('-date_promotion',)


@admin.register(Echelon)
class EchelonAdmin(admin.ModelAdmin):
    list_display = ('fonctionnaire', 'date_echelon', 'ancien_echelon', 'nouvel_echelon')
    search_fields = ('fonctionnaire__nom', 'fonctionnaire__prenom')
    ordering = ('-date_echelon',)
