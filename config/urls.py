from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('leave/', include('leave_management.urls', namespace='leave_management')),
    path('career/', include('career.urls', namespace='career')),
    path('salary/', include('salary_management.urls', namespace='salary_management')),
    path('audit/', include('audit.urls', namespace='audit')),
    path('', lambda request: redirect('login')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = "AU HERMES Administration"
admin.site.site_title = "AU HERMES Admin Portal"
admin.site.index_title = "Welcome to AU HERMES HR Management"