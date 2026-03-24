# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def products(request):
    items = [
        {"name": "Chocolate Cake", "price": 500},
        {"name": "Croissant", "price": 120},
        {"name": "Donut", "price": 80},
    ]
    return render(request, 'products.html', {"items": items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')