from django.db import models
from staff.models import Employee, Fonctionnaire


class CareerHistory(models.Model):
    """Career progression tracking for Administrative Staff"""
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Career History"
        verbose_name_plural = "Career Histories"
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.employee.user.username} - {self.position_title}"


class Promotion(models.Model):
    """Promotion records for Civil Servants"""
    
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    date_promotion = models.DateField()
    ancien_grade = models.CharField(max_length=100, blank=True, null=True)
    nouveau_grade = models.CharField(max_length=100)
    observation = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"
        ordering = ['-date_promotion']
    
    def __str__(self):
        return f"{self.fonctionnaire.nom} - {self.nouveau_grade}"


class Echelon(models.Model):
    """Grade level progression for Civil Servants"""
    
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    date_echelon = models.DateField()
    ancien_echelon = models.IntegerField(blank=True, null=True)
    nouvel_echelon = models.IntegerField()
    observation = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Grade Level"
        verbose_name_plural = "Grade Levels"
        ordering = ['-date_echelon']
    
    def __str__(self):
        return f"{self.fonctionnaire.nom} - Level {self.nouvel_echelon}"
