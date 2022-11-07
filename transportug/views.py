from django.shortcuts import render
from .models import Bus,BusCompany,Prices

# Create your views here.
def home(request):
    companies = BusCompany.objects.all().order_by('region')
    return render(request,'home.html',{
        'companies' : companies
    })

def district(request,region):
    buses = Bus.objects.filter(mainOffices=region)
    return render(request,'region.html',{
        'buses':buses
    })

def company(request,company):
    companydetails = Bus.objects.filter(company=company)
    return render(request,'busCompany.html',{
        'buscompanies' : companydetails
    })

def busShift(request,id):
    shift = Bus.objects.get(id=id)
    return render(request,'busShift.html',{
       'shift': shift,
       'shift_id' : id,
       
    })

def bookShift(request):
    busId = request.POST.get('shift_id')
    shiftSeats = Bus.objects.get(id=busId)
    shiftSeats.seats = int(shiftSeats.seats) - 1
    shiftSeats.save()
    return render(request, 'booked.html')