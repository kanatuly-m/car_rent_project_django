from rest_framework import serializers
from .models import Car, Rental

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'year', 'price_per_day', 'available')

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'car', 'user', 'rental_date', 'return_date')
