from django.urls import path
from .views import home , phones

urlpatterns = [
    path('', home, name = 'main-page'),
    path('myapp/',phones, name = 'phones-page')
]