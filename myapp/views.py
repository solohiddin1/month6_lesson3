from django.shortcuts import render
from .models import Phones
# Create your views here.

def home(request):
    return render(request,'main_page.html') 

def phones(request):
    phones = Phones.objects.all()
    return render(request,'phones.html',{'phones':phones})
