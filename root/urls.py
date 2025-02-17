from django.contrib import admin
from django.urls import path, include

from events.admin import event_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('apps.urls')),
    path('event-admin/', event_admin_site.urls),
]
