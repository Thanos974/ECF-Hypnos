from django.urls import path
from . import views
from .models import Hotel



urlpatterns = [
    path('', views.home_view, name="home"),
    path('hotel/', views.hotel_view, name='hotel'),
    path('suites/', views.suites_view, name='suites'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name="signup"),
    path('book/', views.book_view, name="book"),
    path('cocooning/', views.cocooning_view, name="cocooning"),

]