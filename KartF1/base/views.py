from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from .models import Booking,Circuit,Message,User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
    booking_messages = booking.message_set.all().order_by('-created')
    racers = booking.racers.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            booking=booking,
            body=request.POST.get('body')
        )
        booking.racers.add(request.user)
        return redirect('booking', pk=booking.id)

    context = {'booking': booking, 'booking_messages': booking_messages, 
    'racers' : racers}
    return render(request, 'booking.html', context)

@login_required(login_url='login')
def createBooking(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking_form.html',context)

@login_required(login_url='login')
def updateBooking(request,pk):
    booking = Booking.objects.get(id=pk)
    form = BookingForm(instance=booking)

    if request.user != booking.user:
        return HttpResponse('Not allowed')

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking_form.html',context)

@login_required(login_url='login')
def deleteBooking(request,pk):
    booking = Booking.objects.get(id=pk)

    if request.user != booking.user:
        return HttpResponse('Not allowed')

    if request.method == 'POST':
        booking.delete()
        return redirect('home')
   
    return render(request, 'delete.html', {'obj':booking})

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = {'page': page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'login_register.html', {'form': form})

@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Not allowed')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
   
    return render(request, 'delete.html', {'obj':message})

