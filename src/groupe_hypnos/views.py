
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from groupe_hypnos.models import Hotel
from django.urls import reverse

def home_view(request):
    return render(request, 'groupe_hypnos/home.html')

def hotel_view(request):
    return render(request, 'groupe_hypnos/hotel.html')

def contact_view(request):
    return render(request, 'contact.html')


# def book_view(request):
#     return render(request, 'groupe_hypnos/book.html')



#HOTELS HYPNOS 

def cocooning_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/cocooning.html', context={'hotels': hotel})

def kilimandjaro_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/kilimandjaro.html', context={'hotels': hotel})

def carlton_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/carlton.html', context={'hotels': hotel})

def splendid_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/splendid.html', context={'hotels': hotel})

def meetic_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/meetic.html', context={'hotels': hotel})

def beach_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/beach.html', context={'hotels': hotel})

def casino_royale_view(request):
    hotel = Hotel.objects.all()
    return render(request, 'groupe_hypnos/casino_royale.html', context={'hotels': hotel})




# RGPD

def rgpd_view(request):
    return render(request, 'rgpd.html')

   