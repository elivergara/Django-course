from django.contrib import admin
from .models import Logger,Booking, Customer, Reservation, Menu
from django.forms import ModelForm, RadioSelect

# Register your models here.
admin.site.register(Logger)
admin.site.register(Booking)
admin.site.register(Customer)
admin.site.register(Menu)


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'booth_table': RadioSelect,  # Render as radio buttons
        }

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm

admin.site.register(Reservation, ReservationAdmin)