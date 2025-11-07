from django.db import models
from django.conf import settings
from staff.models import Fonctionnaire


class Historique(models.Model):
    """Action history log"""
    
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    date_action = models.DateTimeField(auto_now_add=True)
    type_action = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"
        ordering = ['-date_action']
    
    def __str__(self):
        return f"{self.fonctionnaire.nom} - {self.type_action}"
