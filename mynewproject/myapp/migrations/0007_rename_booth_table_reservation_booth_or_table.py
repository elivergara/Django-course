# Generated by Django 5.1.4 on 2024-12-13 23:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_reservation_options_reservation_booth_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="booth_table",
            new_name="Booth_or_Table",
        ),
    ]