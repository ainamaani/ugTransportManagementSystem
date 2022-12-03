from django.contrib import admin
from . models import Bus,BusCompany,Prices,BookedCustomers

# Register your models here.

class BusAdmin(admin.ModelAdmin):
    list_display = ("company","numberPlate","mainOffices")
admin.site.register(Bus,BusAdmin)
admin.site.register(BusCompany)
admin.site.register(Prices)
admin.site.register(BookedCustomers)

