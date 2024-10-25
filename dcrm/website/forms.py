from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
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
        fields = ['Arrival_date', 'Departure_date','Hotel_Room','Hotel_adult','Hotel_cost','customer_ID']
        labels ={
            "Hotel_adult": 'Are you over 18?',
        }
    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('customer_ID',None)
        super(BookHotelTicket, self).__init__(*args, **kwargs)
        if user_id is not None:
            self.fields['customer_ID'].queryset = Record.objects.filter(customer_ID=user_id)
        else:
            self.fields['customer_ID'].queryset = Record.objects.none()
class BookZooTicket(forms.ModelForm):
    class Meta:
        model= BookingZoo
        fields = ['valid_date','zoo_adult','zoo_cost']