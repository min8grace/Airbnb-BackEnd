# Generated by Django 4.2.2 on 2023-06-19 08:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0002_room_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
    ]
