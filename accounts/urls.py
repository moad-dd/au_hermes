from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('dashboard/admin/', views.employee_dashboard, name='employee_dashboard'),
    path('edit/', views.edit_account, name='edit_account'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]