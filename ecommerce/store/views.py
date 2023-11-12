from django.shortcuts import render
from .models import Product
from datetime import datetime


# Create your views here.
def home(request):
    current_year = datetime.now().year
    products = Product.objects.all()
    return render(request, "home.html", {'company': "New Gens", 'current_year': current_year, 'products': products})
