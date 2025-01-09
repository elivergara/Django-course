from django.db import models

# Create your models here.
class Person(models.Model):
    Person_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField( max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time")


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
    

BOOTH_TABLE_CHOICES = [('Booth', 'Booth'), ('Table', 'Table')]

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone Number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField(default=None)
    notes = models.CharField(max_length=300, blank=True)
    Booth_or_Table = models.CharField(
        max_length=10,
        choices=BOOTH_TABLE_CHOICES,
        default='Table', 
    )


    def __str__(self):
        return self.name + ' - ' + self.notes

class Menu(models.Model):
    name=models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name