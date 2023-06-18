from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from .models import Booking,Circuit, Equipment,Message, Order,User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import BookingForm
from django.contrib import messages
from django.core.paginator import Paginator

# View for the main page. Contains the query for the searchBar
def home(request):
    page = 'home'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    

    bookings = Booking.objects.filter(Q(circuit__name__icontains=q) |
    Q(name__icontains=q) | Q(user__username__icontains=q))

    circuits = Circuit.objects.all()
    booking_count = bookings.count()
    booking_messages = Message.objects.filter(Q(booking__circuit__name__icontains=q))
    
    booking_paginator = Paginator(bookings, 5)
    page_number = request.GET.get("page")
    page_obj = booking_paginator.get_page(page_number)

    context = {'bookings': bookings, 'circuits': circuits, 
    'booking_count': booking_count, 'booking_messages': booking_messages,
    'page' : page, "page_obj": page_obj}
    return render(request, 'home.html', context)

# Login view
@login_required(login_url='login')
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

# Circuits view
@login_required(login_url='login')
def circuit(request):
    circuits = Circuit.objects.all()

    context = {'circuits': circuits}
    return render(request, 'circuit.html', context)

# Equipment view
@login_required(login_url='login')
def equipment(request):
    equipments = Equipment.objects.all()
    
    context = {'equipments': equipments}
    return render(request, 'equipment.html', context)

# Profile view
@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    bookings = user.booking_set.all()
    booking_messages = user.message_set.all()
    
    booking_paginator = Paginator(bookings, 5)
    page_number = request.GET.get("page")
    page_obj = booking_paginator.get_page(page_number)
    
    circuits = Circuit.objects.all()
    context = {'user': user, 'bookings':bookings,
    'booking_messages': booking_messages, 'circuits': circuits, "page_obj": page_obj }
    return render(request, 'profile.html', context)

# Booking creation view
@login_required(login_url='login')
def createBooking(request):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'booking_form.html',context)

# Booking update view
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

# Booking delete view
@login_required(login_url='login')
def deleteBooking(request,pk):
    booking = Booking.objects.get(id=pk)

    if request.user != booking.user:
        return HttpResponse('Not allowed')

    if request.method == 'POST':
        booking.delete()
        return redirect('home')
   
    return render(request, 'delete.html', {'obj':booking})

# login view
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

# logout view
def logoutUser(request):
    logout(request)
    return redirect('home')

# register view
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

# deleting a message view
@login_required(login_url='login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Not allowed')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
   
    return render(request, 'delete.html', {'obj':message})

# def index(request):
#     return render(request, 'index.html')

# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
    
#     context = {'items':items}
#     return render (request, 'cart.html', context)
