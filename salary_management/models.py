from django.db import models
from staff.models import Fonctionnaire


class Paie(models.Model):
    """Payroll for Civil Servants"""
    
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    mois = models.CharField(max_length=20, verbose_name="Month")
    annee = models.IntegerField(verbose_name="Year")
    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    indemnites = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    retenues = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_a_payer = models.DecimalField(max_digits=10, decimal_places=2)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Salary Slip"
        verbose_name_plural = "Salary Slips"
        unique_together = ['fonctionnaire', 'mois', 'annee']
        ordering = ['-annee', '-mois']
    
    def __str__(self):
        return f"{self.fonctionnaire.nom} - {self.mois}/{self.annee}"


class Prime(models.Model):
    """Bonus/Premium for Civil Servants"""
    
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    type_prime = models.CharField(max_length=100, verbose_name="Bonus Type")
    montant = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")
    date_prime = models.DateField(verbose_name="Date")
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Bonus"
        verbose_name_plural = "Bonuses"
        ordering = ['-date_prime']
    
    def __str__(self):
        return f"{self.fonctionnaire.nom} - {self.type_prime}"
