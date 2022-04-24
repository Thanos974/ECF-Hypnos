from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="home"),
    path('hotel/', views.hotel_view, name='hotel'),
    path('contact/', views.contact_view, name='contact'),
    path('cocooning/', views.cocooning_view, name="cocooning"),
    path('kilimandjaro/', views.kilimandjaro_view, name="kilimandjaro"),
    path('carlton/', views.carlton_view, name="carlton"),
    path('splendid/', views.splendid_view, name="splendid"),
    path('meetic/', views.meetic_view, name="meetic"),
    path('beach/', views.beach_view, name="beach"),
    path('casino_royale/', views.casino_royale_view, name="casino_royale"),
    path('rgpd/', views.rgpd_view, name="rgpd"),
   
]