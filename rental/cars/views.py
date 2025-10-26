# cars/views.py
from django.shortcuts import render, redirect
from .models import Car, Rental
from .forms import PaymentForm  # Если используется форма для платежа
from django.contrib.auth.decorators import login_required
from .forms import RentalForm 


def car_list(request):
    cars = Car.objects.all()  # Получаем все автомобили
    return render(request, 'cars/car_list.html', {'cars': cars})  # Отображаем список автомобилей


@login_required
def rental_form(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)  # Не сохраняем еще
            rental.user = request.user  # Связываем аренду с текущим пользователем
            rental.save()  # Сохраняем аренду
            return redirect('user-profile')  # Перенаправляем на личный кабинет
    else:
        form = RentalForm()

    return render(request, 'cars/rental_form.html', {'form': form})


def car_create(request):
    if request.method == "POST":
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        price_per_day = request.POST['price_per_day']
        available = request.POST.get('available', False)  # Если не указан, то False

        Car.objects.create(make=make, model=model, year=year, price_per_day=price_per_day, available=available)
        return redirect('car-list')  # Перенаправление на страницу списка автомобилей

    return render(request, 'cars/car_create.html')  # Отображаем форму для добавления нового автомобиля

def create_payment(request, rental_id):
    rental = Rental.objects.get(id=rental_id)

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.rental = rental  # Привязываем платеж к аренде
            payment.user = rental.user  # Привязываем платеж к пользователю аренды
            payment.save()
            rental.payment = payment  # Сохраняем связь с оплатой в аренде
            rental.save()
            return redirect('rental-detail', rental_id=rental.id)  # Перенаправляем на деталь аренды
    else:
        form = PaymentForm()

    return render(request, 'cars/create_payment.html', {'form': form, 'rental': rental})

