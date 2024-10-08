from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from charging_stations_app.models import ChargingStation
from booking_app.models import Booking

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_accounts_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
    return render(request, 'user_accounts_app/login.html')


def home(request):
    stations = ChargingStation.objects.all()
    bookings = []

    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)

    return render(request, 'user_accounts_app/home.html', {'station': stations, 'bookings': bookings})



