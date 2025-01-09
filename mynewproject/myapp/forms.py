from django import forms
from django.forms.widgets import NumberInput
from .models import Booking, Customer

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

FAVORITE_DISH = [
    ('Italian', 'Italian'),
    ('greek', 'Greek'),
    ('Chinese', 'Chinese'),
    ('Mexican', 'Mexican'),
    ('Indian', 'Indian')
]
GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

class DemoForm(forms.Form):
    new_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label= 'Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label='Email')
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    favorite_dish1 = forms.ChoiceField(choices=FAVORITE_DISH) #rDropdown
    favorite_dish2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_DISH) #Radio buttons


class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    posts = (('Manager', 'Manager'), ('Cashier', 'Cashier'), ('Operator', 'Operator'))
    first_name = forms.CharField(label="Enter first name", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(min_value=20, max_value=60, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

from .models import Logger
class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"