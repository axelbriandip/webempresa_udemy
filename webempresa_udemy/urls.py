from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Paths de core
    path('', include('core.urls')),

    # Paths de admin
    path('admin/', admin.site.urls),
]
