from django.urls import path
from . import views



urlpatterns = [
   
  path('book/', views.book_view, name="book"),
  path('suite', views.suite_view, name="suite"),
]
