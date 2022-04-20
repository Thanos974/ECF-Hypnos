from django.urls import path
from . import views


urlpatterns = [
  
  path('', views.suites, name='suites'),
  path('suite_saint_honore/', views.suite_saint_honore, name="suite_saint_honore"),
  path('suite_deluxe/', views.suite_deluxe, name="suite_deluxe"),
  path('suite_royale/', views.suite_royale, name="suite_royale"),
  path('suite_presidentielle/', views.suite_presidentielle, name="suite_presidentielle"),
  path('suite_penthouse/', views.suite_penthouse, name="suite_penthouse"),
  path('suite_lumiere/', views.suite_lumiere, name="suite_lumiere"),
  path('suite_imperiale/', views.suite_imperiale, name="suite_imperiale"),
  path('suite_honeymoon/', views.suite_honeymoon, name="suite_honeymoon"),
  path('suite_prestige_jr/', views.suite_prestige_jr, name="suite_prestige_jr"),
  path('suite_superieure/', views.suite_superieure, name="suite_superieure"),
   
   
]