from django.urls import path
from . import views

app_name = 'leave_management'

urlpatterns = [
    path('request/', views.leave_request, name='leave_request'),
    path('civil-servants/<int:pk>/leave/', views.update_leave, name='update_leave'),
    path('civil-servants/<int:pk>/leave-certificate/', views.print_leave_certificate, name='print_leave_certificate'),
]