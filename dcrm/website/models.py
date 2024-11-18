from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     loyalty_points = models.IntegerField(default=0)
#     creation_data = models.DateTimeField(auto_now_add= True)
#     customer_ID = models.AutoField(primary_key=True, editable=False)
#     first_name = models.CharField(max_length = 20)
#     last_name = models.CharField(max_length = 50)
#     email = models.CharField(max_length = 50)
#     phone = models.CharField(max_length=20)
#     postcode = models.CharField(max_length=10)
#     street_name = models.CharField(max_length = 20)
#     city = models.CharField(max_length = 50)
#     house_number = models.CharField(max_length=10)

# Create your models here.
class Record(AbstractUser):

    loyalty_points = models.IntegerField(default=0)
    creation_data = models.DateTimeField(auto_now_add= True)
    # first_name = models.CharField(max_length = 20)
    # last_name = models.CharField(max_length = 50)
    # email = models.CharField(max_length = 50)
    phone = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    street_name = models.CharField(max_length = 20)
    city = models.CharField(max_length = 50)
    house_number = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.first_name + " " + self.last_name
#  fields = ['first_name','last_name','email','phone','postcode','street_name','city','house_number']

class BookingHotel(models.Model):
    creation_data = models.DateTimeField(auto_now_add=True)
    booking_ID = models.AutoField(primary_key=True, editable=False)
    Arrival_date = models.DateField(max_length=10)
    Departure_date = models.DateField(max_length=10)
    Hotel_Room = models.CharField(max_length=5)
    Hotel_adult = models.BooleanField()
    Hotel_cost = models.IntegerField(default=0)
    customer_ID = models.ForeignKey(Record, on_delete=models.CASCADE)

class BookingZoo(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    admission_ID = models.AutoField(primary_key=True, editable=False)
    valid_date = models.DateField(max_length=10)
    zoo_adult = models.IntegerField(default=0)
    zoo_child = models.IntegerField(default=0)
    zoo_cost = models.IntegerField(default=10)
    points = models.IntegerField(default=0)
    customer_ID = models.ForeignKey(Record, on_delete=models.CASCADE)