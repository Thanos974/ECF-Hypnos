from tokenize import group
from django.shortcuts import render
from django.views.generic import ListView
from groupe_hypnos.models import Hotel


def home_view(request):
    return render(request, 'home.html')

def hotel_view(request):
    return render(request, 'hotel.html')

def suites_view(request):
    return render(request, 'suites.html')

def contact_view(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def book_view(request):
    return render(request, 'book.html')

def cocooning_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/cocooning.html', context={'hotels': hotel})



   