from django.shortcuts import render
from datetime import datetime

current_year = datetime.now().year


# Create your views here.
def cart_summary(request):
    return render(request, "cart.html", {'company': "New Gens", 'current_year': current_year})


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass
