from django import forms
from .models import ChargingStation

class ChargingStationForm(forms.ModelForm):
    class Meta:
        model = ChargingStation
        fields = ['name','location','total_slots','available_slots','charging_slots']
