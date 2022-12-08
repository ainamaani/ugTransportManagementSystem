from django.shortcuts import render,redirect
from .models import Bus,BusCompany,Prices,BookedCustomers
from django.contrib import messages
from django.contrib.auth.models import User,auth
from datetime import datetime

# Create your views here.
#Registration
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.info('Passwords not matching')
            return redirect(request.build_absolute_uri('/ugtransport/register'))
        if User.objects.filter(email=email).exists():
            messages.info('Email already exists')
            return redirect(request.build_absolute_uri('/ugtransport/register'))
        elif User.objects.filter(username=username).exists():
            messages.info('Username already taken')
            return redirect(request.build_absolute_uri('/ugtransport/register'))
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            return redirect(request.build_absolute_uri('/ugtransport/login'))

    return render(request,'register.html')

#Login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(request.build_absolute_uri('/ugtransport/district'))
        else:
            messages.info('Invalid Credentials')
            return redirect(request.build_absolute_uri('/ugtransport/login'))
    return render(request, 'login.html')

#Displaying the districts
def home(request):
    companies = BusCompany.objects.all().order_by('region')
    return render(request,'home.html',{
        'companies' : companies
    })

#Display the buses in each region
def district(request,region):
    buses = Bus.objects.filter(mainOffices=region)
    return render(request,'region.html',{
        'buses':buses
    })

#Display bus details(shifts) with book button
def company(request,company):
    companydetails = Bus.objects.filter(company=company)
    return render(request,'busCompany.html',{
        'buscompanies' : companydetails
    })

#Booking page for a single shift
def busShift(request,id):
    shift = Bus.objects.get(id=id)
    return render(request,'busShift.html',{
       'shift': shift,
       'shift_id' : id,
       
    })

#On booking the shift
def bookShift(request):
    busId = request.POST.get('shift_id')
    shiftSeats = Bus.objects.get(id=busId) #shiftSeats is just an object
    shiftSeats.seats = int(shiftSeats.seats) - 1
    shiftSeats.totalTickets = int(shiftSeats.totalTickets) - 1
    shiftSeats.save() #save the object

    userId = request.user.id
    user = User.objects.get(id=userId)
    busBooked = shiftSeats.company
    busNumberPlate = shiftSeats.numberPlate
    seatNumber = shiftSeats.seats
    totalTickets = shiftSeats.totalTickets
    
    # shiftBooked = shiftSeats.travelTime
    # shift = Bus.objects.get(travelTime=shiftBooked)

    customerBooking = BookedCustomers.objects.create(customer=user,busBooked=busBooked,
    ticketNumber=totalTickets,seatNumber=seatNumber,bookingDate=datetime.now(),
    busNumberPlate=busNumberPlate)
    customerBooking.save()
    return render(request, 'booked.html')

# Getting the tickets
