from django.urls import path
from . import views

app_name = 'audit'

urlpatterns = [
    path('civil-servants/<int:pk>/history/', views.view_history, name='view_history'),
]