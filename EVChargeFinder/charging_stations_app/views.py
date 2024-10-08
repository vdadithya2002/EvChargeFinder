from django.shortcuts import render, get_object_or_404, redirect
from .models import ChargingStation
from .forms import ChargingStationForm

def station_list(request):
    stations = ChargingStation.objects.all()
    return render(request, 'charging_stations_app/station_list.html',{'stations': stations})


def add_station(request):
    if request.method == 'POST':
        form = ChargingStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('station_list')
    else:
        form = ChargingStationForm()
    return render(request, 'charging_stations_app/add_station.html', {'form': form})

#updating an existing charging station
def update_station(request,station_id):
    station = get_object_or_404(ChargingStation, pk=station_id)
    if request.method == 'POST' :
        form = ChargingStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('station_list')
    else:
        form = ChargingStationForm(instance=station)
    return render(request, 'charging_stations_app/update_station.html', {'form': form})

#delete a charging station
def delete_station(request, station_id):
    station = get_object_or_404(ChargingStation, pk=station_id)
    if request.method == 'POST':
        station.delete()
        return redirect('station_list')
    return render(request, 'charging_stations_app/delete_station.html', {'station':station})        

        


