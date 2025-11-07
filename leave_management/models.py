from django.db import models
from django.conf import settings
from staff.models import Employee, Fonctionnaire


class LeaveRequest(models.Model):
    """Leave Request Model for Administrative Staff"""
    
    LEAVE_TYPES = [
        ('ANNUAL', 'Annual Leave'),
        ('SICK', 'Sick Leave'),
        ('UNPAID', 'Unpaid Leave'),
        ('MATERNITY', 'Maternity Leave'),
        ('PATERNITY', 'Paternity Leave'),
        ('OTHER', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES, default='ANNUAL')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_submitted = models.DateField(auto_now_add=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_leaves'
    )
    
    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"
        ordering = ['-date_submitted']
    
    def __str__(self):
        return f"{self.employee.user.username} - {self.get_leave_type_display()} ({self.status})"
    
    @property
    def duration(self):
        return (self.end_date - self.start_date).days + 1


class Conge(models.Model):
    """Leave records for Civil Servants"""
    
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.CASCADE)
    type_conge = models.CharField(max_length=100, verbose_name="Leave Type")
    date_debut = models.DateField(verbose_name="Start Date")
    date_fin = models.DateField(verbose_name="End Date")
    motif = models.TextField(verbose_name="Reason")
    
    class Meta:
        verbose_name = "Leave"
        verbose_name_plural = "Leaves"
        ordering = ['-date_debut']
    
    def __str__(self):
        return f"{self.fonctionnaire.nom} - {self.type_conge}"
