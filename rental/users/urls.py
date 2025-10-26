# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', user_views.home, name='home'),  
]
