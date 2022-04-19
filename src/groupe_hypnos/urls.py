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
    path('kilimandjaro/', views.kilimandjaro_view, name="kilimandjaro"),
    path('carlton/', views.carlton_view, name="carlton"),
    path('splendid/', views.splendid_view, name="splendid"),
    path('meetic/', views.meetic_view, name="meetic"),
    path('beach/', views.beach_view, name="beach"),
    path('casino_royale/', views.casino_royale_view, name="casino_royale"),
    path('rgpd/', views.rgpd_view, name="rgpd"),
   
]