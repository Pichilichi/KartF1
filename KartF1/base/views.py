from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Booking,Circuit
from .forms import BookingForm

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    bookings = Booking.objects.filter(Q(circuit__name__icontains=q) |
    Q(name__icontains=q) | Q(user__username__icontains=q))

    circuits = Circuit.objects.all()
    booking_count = bookings.count()

    context = {'bookings': bookings, 'circuits': circuits, 'booking_count': booking_count}
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