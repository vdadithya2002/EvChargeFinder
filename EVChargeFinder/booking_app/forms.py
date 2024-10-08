from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['charging_station', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # This remains a date input
            'start_time': forms.TimeInput(attrs={'type': 'time'}),  # Use TimeInput for time-only input
            'end_time': forms.TimeInput(attrs={'type': 'time'}),    # Use TimeInput for time-only input
        }
