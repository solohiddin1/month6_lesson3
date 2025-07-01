from .views import laptops 
from django.urls import path

urlpatterns = [
    path('',laptops, name = 'laptops-page')
]