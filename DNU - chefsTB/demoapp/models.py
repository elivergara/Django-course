from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, default=None)
    reservation_day = models.CharField(max_length=10, default=None)
    seats = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
