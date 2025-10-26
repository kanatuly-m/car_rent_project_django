# users/forms.py
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_admin']


