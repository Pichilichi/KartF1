from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking,Category
from .forms import BookingForm

def home(request):
    bookings = Booking.objects.all()

    categories = Category.objects.all()

    context = {'bookings': bookings, 'categories': categories}
    return render(request, 'home.html', context)

def booking(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {'booking': booking}
    return render(request, 'booking.html', context)

def createBooking(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking_form.html',context)

def updateBooking(request,pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking_form.html',context)

def deleteBooking(request,pk):
    booking = Booking.objects.get(id=pk)

    if request.method == 'POST':
        booking.delete()
        return redirect('home')
    
    return render(request, 'delete.html', {'obj':booking})