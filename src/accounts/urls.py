from django.urls import path
from accounts.views import signup, login_user, logout_user, dashboard



urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name="logout"),
    path('dashboard/', dashboard, name='dashboard') 
]   