from django.shortcuts import render



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