from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Order


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'address', 'phone_number', 'image']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item_name', 'quantity', 'price']