from django.forms import ModelForm
from .models import Booking

from django import forms
from django.contrib.auth.models import User


# Code added for loading form data on the Booking page
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']








class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
