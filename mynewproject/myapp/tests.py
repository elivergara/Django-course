from django.test import TestCase
from datetime import datetime
from .models import Reservation
# Create your tests here.

class ReservationModelTest(TestCase):

    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            name='Eli Vergara',
            contact='520-280-9601',

        )

def test_fields(self):
    self.assertIsInstance(self.reservation.name,  str)
    self.assertIsInstance(self.reservation.contact, str)

def test_timestamps(self):
    self.assertIsInstance(self.reservation.time, datetime)