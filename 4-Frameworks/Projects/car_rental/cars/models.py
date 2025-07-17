from django.db import models

class Car(models.Model):

    class Type(models.TextChoices):
        SUV = ('SUV', 'Sport Utility Vehicle')
        SEDAN = ('SEDAN', 'Standard Sedan')
        HATCHBACK = ('HATCHBACK', 'Compact Hatchback')
        COUPE = ('COUPE', 'Two-door Coupe')
        CONVERTIBLE = ('CONVERTIBLE', 'Convertible')
        VAN = ('VAN', 'Van')
        MINIVAN = ('MINIVAN', 'Minivan')
        PICKUP_TRUCK = ('PICKUP_TRUCK', 'Pickup Truck')
        MOTORCYCLE = ('MOTORCYCLE', 'Motorcycle')

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    reg_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(choices=Type.choices)
    vin_number = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.name} - {self.reg_number}"
    