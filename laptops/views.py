from django.shortcuts import render
from .models import Laptops
# Create your views here.

def laptops(request):
    laptops = Laptops.objects.all()
    return render(request,'laptops/laptops_page.html',{'laptops':laptops})
