# Generated by Django 5.2.4 on 2025-07-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("name", models.CharField(max_length=100)),
                ("brand", models.CharField(max_length=100)),
                ("year", models.IntegerField(max_length=4)),
                ("reg_number", models.CharField(max_length=20)),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("SUV", "Sport Utility Vehicle"),
                            ("SEDAN", "Standard Sedan"),
                            ("HATCHBACK", "Compact Hatchback"),
                            ("COUPE", "Two-door Coupe"),
                            ("CONVERTIBLE", "Convertible"),
                            ("VAN", "Van"),
                            ("MINIVAN", "Minivan"),
                            ("PICKUP_TRUCK", "Pickup Truck"),
                            ("MOTORCYCLE", "Motorcycle"),
                        ]
                    ),
                ),
                ("vin_number", models.CharField(max_length=25)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("availability", models.BooleanField(default=True)),
            ],
        ),
    ]
