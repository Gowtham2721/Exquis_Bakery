from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('about/', views.about),
    path('contact/', views.contact),
]