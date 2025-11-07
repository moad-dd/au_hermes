from django.db import models
from django.conf import settings
from datetime import date


class Fonctionnaire(models.Model):
    """Civil Servant Employee Model"""
    
    STATUS_CHOICES = [
        ('Actif', 'Active'),
        ('Congé', 'On Leave'),
        ('Retraité', 'Retired'),
        ('Démissionné', 'Resigned'),
    ]
    
    ss = models.CharField(max_length=20, unique=True, verbose_name="Social Security Number")
    nom = models.CharField(max_length=50, verbose_name="Last Name")
    prenom = models.CharField(max_length=50, verbose_name="First Name")
    grade = models.CharField(max_length=100, verbose_name="Grade")
    date_rec = models.DateField(verbose_name="Recruitment Date")
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Actif')
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    photo = models.ImageField(upload_to='employees/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Civil Servant"
        verbose_name_plural = "Civil Servants"
        ordering = ['-date_rec']
    
    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.grade}"


class Employee(models.Model):
    """Administrative Staff Model (ATS)"""
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, verbose_name="Position")
    department = models.CharField(max_length=100, blank=True, null=True)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_hired = models.DateField(default=date.today, verbose_name="Hire Date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Administrative Staff"
        verbose_name_plural = "Administrative Staff"
        ordering = ['-date_hired']
    
    def __str__(self):
        return f"{self.user.username} - {self.position}"
    
    @property
    def total_salary(self):
        return self.base_salary + self.bonus - self.deductions
