
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('studi/', admin.site.urls),
    path('', include('groupe_hypnos.urls')),
    path('accounts/', include('accounts.urls')),    
    path('accounts/', include('django.contrib.auth.urls')),   
    path('suites/', include('suites.urls')), 
    path('reservation/', include('reservation.urls')), 
    # path('remerciements/', views.remerciements.view, name="remerciements"),

] 
