from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    items = [
        {"name": "Chocolate Cake", "image": "images/pic01.jpg", "price": 500},
        {"name": "Croissant", "image": "images/pic02.jpg", "price": 120},
        {"name": "Donut", "image": "images/pic03.jpg", "price": 80},
        {"name": "Cupcake", "image": "images/pic04.jpg", "price": 60},
        {"name": "Bread", "image": "images/pic05.jpg", "price": 40},
        {"name": "Pastry", "image": "images/pic06.jpg", "price": 90},
    ]

    return render(request, 'products.html', {"items": items})