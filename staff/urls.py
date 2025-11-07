from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('onboard/', views.onboard_employee, name='onboard_employee'),
    path('civil-servants/', views.civil_servants_list, name='civil_servants_list'),
    path('civil-servants/add/', views.add_civil_servant, name='add_civil_servant'),
    path('civil-servants/<int:pk>/', views.civil_servant_detail, name='civil_servant_detail'),
    path('civil-servants/<int:pk>/edit/', views.edit_civil_servant, name='edit_civil_servant'),
    path('civil-servants/<int:pk>/delete/', views.delete_civil_servant, name='delete_civil_servant'),
    path('ats/', views.list_ats, name='list_ats'),
    path('ats/<int:pk>/delete/', views.delete_ats, name='delete_ats'),
    path('space/', views.user_space, name='user_space'),
    path('ats-space/', views.ats_space, name='ats_space'),
]