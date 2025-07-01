from django.urls import path
from .views import home , phones , about_us, contact_us

urlpatterns = [
    # path('', home, name = 'main-page'),
    path('',phones, name = 'phones-page'),
    path('about-us',about_us, name = 'about-us'),
    path('contact-us',contact_us, name = 'contact-us'),
]