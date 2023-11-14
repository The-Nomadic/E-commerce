from django.shortcuts import render, redirect
from .models import Product, Category
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

current_year = datetime.now().year


def category(request, cat):
    cat = cat.replace('-', ' ')
    try:
        categories = Category.objects.all()
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, "category.html", {'company': "New Gens", 'current_year': current_year,
                                                 'products': products, 'category': category,
                                                 'categories': categories})
    except:
        messages.success(request, f"{cat} doesn't exist")
        return redirect('home')


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'company': "New Gens", 'current_year': current_year, 'products': products})


def about(request):
    return render(request, "about.html", {'company': "New Gens", 'current_year': current_year})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Success")
            return redirect('home')
        else:
            messages.success(request, "Something went wrong, Try again")
            return redirect('login')
    else:
        return render(request, "login.html", {'company': "New Gens", 'current_year': current_year})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # lig in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account Created")
            return redirect('home')
        else:
            messages.success(request, "Sorry, Some Error Occurred")
            return redirect('register')
    else:
        return render(request, "register.html", {'company': "New Gens", 'current_year': current_year, 'form': form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'company': "New Gens", 'current_year': current_year, 'product': product})
