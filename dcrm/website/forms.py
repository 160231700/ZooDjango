from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record, BookingHotel, BookingZoo

class CreateUserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','postcode','street_name','city','house_number']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','postcode','street_name','city','house_number']

class BookHotelTicket(forms.ModelForm):
    class Meta:
        model = BookingHotel
        fields = ['Arrival_date', 'Departure_date','Hotel_Room','Hotel_adult','Hotel_cost']
        labels ={
            "Hotel_adult": 'Are you over 18?',
        }

class BookZooTicket(forms.ModelForm):
    class Meta:
        model= BookingZoo
        fields = ['valid_date','zoo_adult','zoo_cost']