from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=50)  
    model = models.CharField(max_length=50)  
    year = models.PositiveIntegerField()  
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)  
    available = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    rental_date = models.DateTimeField(auto_now_add=True) 
    return_date = models.DateTimeField()  

    def __str__(self):
        return f"{self.user.username} rented {self.car.make} {self.car.model}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, который оплатил
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE)  # Ссылка на аренду
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма
    paid_at = models.DateTimeField(auto_now_add=True)  # Время платежа
    method = models.CharField(max_length=100)  # Способ оплаты (например, карта, PayPal)

    def __str__(self):
        return f"Payment {self.id} for {self.rental.car.make} - {self.amount} USD"
