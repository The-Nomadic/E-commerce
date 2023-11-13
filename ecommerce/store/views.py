from django.shortcuts import render
from .models import Product
from datetime import datetime

current_year = datetime.now().year


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'company': "New Gens", 'current_year': current_year, 'products': products})


def about(request):
    return render(request, "about.html", {'company': "New Gens", 'current_year': current_year})
