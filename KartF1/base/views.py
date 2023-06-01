from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking

def home(request):
    bookings = Booking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'home.html', context)

def booking(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {'booking': booking}
    return render(request, 'booking.html', context)

def createBooking(request):
    context = {}
    return render(request, 'booking_form.html',context)