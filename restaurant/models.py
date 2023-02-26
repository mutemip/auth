from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

   class Meta:
      db_table = 'booking'


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.TextField(null=True)

   def __str__(self):
      return self.name

   class Meta:
      db_table = 'menu'