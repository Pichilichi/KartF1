from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Booking,Circuit,User
from django.contrib.auth import authenticate,login,logout
from .forms import BookingForm
from django.contrib import messages

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

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')