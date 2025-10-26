# users/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from cars.models import Rental
from django.contrib.auth import login
from cars.models import Car



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Авторизуем пользователя
            return redirect('home')  # Переход на главную страницу после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    rentals = Rental.objects.filter(user=request.user)  # Предполагается, что у Rental есть поле "user"
    return render(request, 'users/profile.html', {'rentals': rentals})


def home(request):
    cars = Car.objects.all()  # Получаем список автомобилей
    return render(request, 'home.html', {'cars': cars})
