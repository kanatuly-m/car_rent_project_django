# users/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from cars.models import Rental



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем на страницу логина
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    rentals = Rental.objects.filter(user=request.user)  # Предполагается, что у Rental есть поле "user"
    return render(request, 'users/profile.html', {'rentals': rentals})
