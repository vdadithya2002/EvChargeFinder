from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the user who is making the booking
            booking.start_time = start_time
            booking.end_time = end_time
            booking.status = 'Booked'
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_app/add_booking.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_app/booking_list.html', {'booking': bookings})
