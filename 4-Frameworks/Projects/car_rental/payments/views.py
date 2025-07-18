from django.shortcuts import render, redirect, get_object_or_404
from bookings.models import Booking
from payments.models import Payment

def pay(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        Payment.objects.create(
            booking=booking,
            amount_paid=booking.total_price(),
            status="success",
        )
        booking.confirmed = True
        booking.save()
        booking.car.availability = False
        return redirect("payments:success")
    return render(request, "payments/confirm_payment.html", {"booking": booking})