from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("confirm/<int:booking_id>/", views.pay, name="pay"),
]