from django.db import models

# Create your models here.
class Record(models.Model):

    creation_data = models.DateTimeField(auto_now_add= True)

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    street_name = models.CharField(max_length = 20)
    city = models.CharField(max_length = 50)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name
#  fields = ['first_name','last_name','email','phone','postcode','street_name','city','house_number']
