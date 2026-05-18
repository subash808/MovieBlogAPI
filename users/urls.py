from django.urls import path
from .views import register, login, profile, logOut

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('profile/', profile, name = 'profile'),
    path('logout/', logOut, name = 'logout')
]