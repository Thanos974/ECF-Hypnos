from django.urls import path
from . import views
# from .views import RoomList, BookingList

# app_name = 'reservation'

urlpatterns = [
   
  path('book/', views.book_view, name="book"),
  # path('room_list', RoomList.as_view(), name='Room_list'),
  # path('bookingList', RoomList.as_view(), name='Booking_list')
    
]
