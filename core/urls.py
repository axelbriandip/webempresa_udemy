from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('store/', views.store, name='store'),
]
