from .views import laptops 
from django.urls import path

urlpatters = [
    path('',laptops, name = 'laptops-page')
]