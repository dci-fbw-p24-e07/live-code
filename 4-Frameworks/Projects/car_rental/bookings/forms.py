from django import forms
from .models import Booking

class BookingForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={
        "type": "date"}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={
        "type": "date"}))
    