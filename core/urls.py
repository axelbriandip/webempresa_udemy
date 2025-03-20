from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample'),
    path('store/', views.store, name='store'),
]