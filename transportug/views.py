from django.shortcuts import render
from .models import Bus,BusCompany,Prices

# Create your views here.
def home(request):
    companies = BusCompany.objects.all()
    return render(request,'home.html',{
        'companies' : companies
    })