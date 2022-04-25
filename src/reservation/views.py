from datetime import datetime
from django.shortcuts import render

from reservation.models import Booking



# Create your views here.


def book_view(request):
    # if request.method == 'POST':
    #     if Booking.is_valid():
    #         Booking.save()
    # else:
    #     init_values = {}
    #     if request.user.is_authenticated():
    #         init_values["hotel"] = request.user
    #         init_values["suite"] = request.user
    #     init_values["checkin"] = datetime.today()
    return render(request, 'reservation/book.html')


