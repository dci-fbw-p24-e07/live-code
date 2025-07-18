from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from cars.models import Car

def create_booking(request, car_id):
    # Retrieve the car
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get the date values
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]

            # Create the booking
            booking = Booking.objects.create(
                customer=request.user,
                car=car,
                start_date=start_date,
                end_date=end_date,
                confirmed=False
            )
            return redirect("payments:pay", booking.id)
    form = BookingForm()
    return render(request, "bookings/book.html", {
        "car": car, "form": form
    })
