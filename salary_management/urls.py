from django.urls import path
from . import views

app_name = 'salary'

urlpatterns = [
    path('slip/', views.salary_slip, name='salary_slip'),
    path('civil-servants/<int:pk>/salary/', views.update_salary, name='update_salary'),
    path('civil-servants/<int:pk>/bonus/', views.update_bonus, name='update_bonus'),
    path('civil-servants/<int:pk>/salary-slip/', views.print_salary_slip, name='print_salary_slip'),
]