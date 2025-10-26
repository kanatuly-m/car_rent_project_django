# cars/forms.py
from django import forms
from .models import Payment
from .models import Rental
from .models import Car

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'method']  # Поля, которые должны быть в форме (сумма и метод)

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'user', 'return_date']  # Пример полей

    car = forms.ModelChoiceField(queryset=Car.objects.all(), empty_label="Choose a car", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(available=True)  # Пример выбора доступных машин
