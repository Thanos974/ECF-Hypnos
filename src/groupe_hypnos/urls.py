from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('hotel/', views.hotel_view, name='hotel'),
    path('suites/', views.suites_view, name='suites'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
]