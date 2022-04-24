from django.shortcuts import render

# from .models import Room, Booking

# Create your views here.
# class RoomList(ListView):
#   model=Room


def book_view(request):
    return render(request, 'reservation/book.html')