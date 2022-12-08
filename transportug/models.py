from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.

    
class BusCompany(models.Model):
    companyName = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    shiftsTo = models.IntegerField()
    shiftsFrom = models.IntegerField()

    def __str__(self) -> str:
        return self.companyName

class Bus(models.Model):
    company = models.CharField(max_length=40)
    numberPlate = models.CharField(max_length=30)
    mainOffices = models.CharField(max_length=30)
    # busImage = models.ImageField(null=True,upload_to='buses')
    destination = models.ForeignKey(BusCompany,related_name='regions',on_delete=models.DO_NOTHING)
    travelTime = models.TimeField()
    seats = models.IntegerField()
    totalTickets = models.CharField(max_length=2,default=64)
    status = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.mainOffices

class Prices(models.Model):
    startLocation = models.ForeignKey(BusCompany,on_delete=models.DO_NOTHING)
    destination = models.CharField(max_length=30)
    price = models.IntegerField()
    busCompany = models.CharField(max_length=30)
    setOffTime = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.busCompany


class BookedCustomers(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    busBooked = models.CharField(max_length=30,null=True)
    shiftBooked = models.DateTimeField(null=True)
    ticketNumber = models.CharField(max_length=30,null=True)
    busNumberPlate = models.CharField(max_length=30,null=True)
    bookingDate = models.DateTimeField(null=True)
    seatNumber = models.CharField(max_length=6,null=True)

    def __str__(self) -> str:
        return self.busBooked
    
