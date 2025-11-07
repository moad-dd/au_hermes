from django.urls import path
from . import views

app_name = 'career'

urlpatterns = [
    path('history/', views.career_history, name='career_history'),
    path('civil-servants/<int:pk>/promotion/', views.update_promotion, name='update_promotion'),
    path('civil-servants/<int:pk>/grade-level/', views.update_grade_level, name='update_grade_level'),
    path('civil-servants/<int:pk>/work-certificate/', views.print_work_certificate, name='print_work_certificate'),
]