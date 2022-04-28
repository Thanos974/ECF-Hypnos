from django.shortcuts import render
from suites.models import Suite
from .import views



#Suites 
def suites(request):
    return render(request, 'suites/suites.html')

def suite_saint_honore(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_saint_honore.html', context={'suites':suite})

def suite_deluxe(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_deluxe.html', context={'suites':suite})

def suite_honeymoon(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_honeymoon.html', context={'suites':suite})

def suite_imperiale(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_imperiale.html', context={'suites':suite})


def suite_lumiere(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_lumiere.html', context={'suites':suite})


def suite_penthouse(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_penthouse.html', context={'suites':suite})


def suite_presidentielle(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_presidentielle.html', context={'suites':suite})

def suite_prestige_jr(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_prestige_jr.html', context={'suites':suite})

def suite_royale(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_royale.html', context={'suites':suite})

def suite_superieure(request):
    suite = Suite.objects.all()
    return render(request, 'suites/suite_superieure.html', context={'suites':suite})


