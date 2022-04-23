from django.shortcuts import render

# from .models import Room, Booking

# Create your views here.
# class RoomList(ListView):
#   model=Room



def booking(request):
  return render(request, 'reservation/booking.html')


