# Generated by Django 5.1.4 on 2024-12-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demoapp", "0004_remove_vehicle_customer_customer_reservation_day_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("guest_count", models.IntegerField()),
                ("reservation_time", models.DateField(auto_now=True)),
                ("comments", models.CharField(max_length=1000)),
            ],
        ),
    ]