from datetime import datetime
from django.shortcuts import render
from groupe_hypnos.models import Hotel
from reservation.models import Booking
from suites.models import Suite



# Create your views here.


# def book_view(request):
#     # if request.method == 'POST':
#     #     if Booking.is_valid():
#     #         Booking.save()
#     # else:
#     #     init_values = {}
#     #     if request.user.is_authenticated():
#     #         init_values["hotel"] = request.user
#     #         init_values["suite"] = request.user
#     #     init_values["checkin"] = datetime.today()
#     return render(request, 'reservation/book.html')




def book_view(request):
    hotels = Hotel.objects.all()
    return render(request, 'reservation/book.html', {"data":hotels})

# def suite_view(request):
#     suites = Suite.objects.all()
#     return render(request, 'reservation/book.html',{"data": suites})
    
