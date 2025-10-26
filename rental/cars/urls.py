# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car-list'),  # Страница списка автомобилей
    path('rental/', views.rental_form, name='rental-create'),  # Страница аренды
    path('cars/create/', views.car_create, name='car-create'),  # Страница для создания автомобиля
    path('payment/<int:rental_id>/', views.create_payment, name='create-payment'),  # Страница оплаты
]
