from django.shortcuts import render


def index(request):
  return render(request, 'groupe_hypnos/hotel.html')

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