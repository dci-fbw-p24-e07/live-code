from django.db import models
from users.models import CustomUser
from cars.models import Car


class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer} - {self.car} - {self.start_date}"

    def total_days(self):
        return (self.end_date - self.start_date).days + 1

    def total_price(self):
        return self.total_days() * self.car.price
