from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Paths de core
    path('', include('core.urls')),
    # Paths of services
    path('services/', include('services.urls')),
    # Paths of blog
    path('blog/', include('blog.urls')),
    # Paths de admin
    path('admin/', admin.site.urls),
]

# si está en modo debug..
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)