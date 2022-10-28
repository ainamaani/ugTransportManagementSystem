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