from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Record, BookingHotel, BookingZoo
from datetime import datetime

class CreateUserForm(UserCreationForm):

    class Meta:
        model=Record
        fields=['password1','password2','username','first_name','last_name','email','phone','postcode','street_name','city','house_number']

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
        widgets = {
            'Arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'Departure_date': forms.DateInput(attrs={'type': 'date'}),
            'Hotel_cost': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Arrival_date'].widget.attrs.update({"input":"Date"})
        # def clean(self):
        #     cleaned_data = super().clean()
        #     Arrival_date = cleaned_data.get('Arrival_date')
        #     Departure_date = cleaned_data.get('Departure_date')


        #     if Departure_date < Arrival_date:
        #         raise forms.ValidationError("End date cannot be earlier than start date.")

        #     time_difference = Departure_date - Arrival_date
        #     cleaned_data['total_cost'] = time_difference.days * 100  # Adjust rate as needed

        # pass
        # Arrival_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # def __init__(self, *args, **kwargs):
    #     user_id = kwargs.pop('customer_ID',None)
    #     super(BookHotelTicket, self).__init__(*args, **kwargs)
    #     if user_id is not None:
    #         self.fields['customer_ID'].queryset = Record.objects.filter(customer_ID=user_id)
    #     else:
    #         self.fields['customer_ID'].queryset = Record.objects.none()
class BookZooTicket(forms.ModelForm):
    class Meta:
        model= BookingZoo
        fields = ['valid_date','zoo_adult','zoo_child','zoo_cost','points']

        labels = {
            "valid_date": "What day you wish to enter the zoo",
            "zoo_adult": "How many adults is this ticket is valid for?",
            "zoo_child": "How many children is this ticket valid for?",
            "points": "How many loyalty points this purchase will generate"
        }
        widgets = {
            "valid_date":forms.DateInput(attrs={'type':'date'}),
            "points": forms.HiddenInput(),
            "zoo_cost": forms.HiddenInput(),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)