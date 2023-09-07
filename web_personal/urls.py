from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about_me, name="about-me"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

# Si estamos en debug=true, ¿Qué hacer con las imgs?
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)