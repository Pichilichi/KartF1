from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

def home(request):
    bookings = Booking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'home.html', context)

def booking(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {'booking': booking}
    return render(request, 'booking.html', context)

def createBooking(request):
    form = BookingForm()
    context = {'form': form}
    return render(request, 'booking_form.html',context)