from . import views
from django.urls import path

urlpatterns = [
    path('trial/',views.home,name='home')
]