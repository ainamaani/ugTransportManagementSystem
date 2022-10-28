from . import views
from django.urls import path

urlpatterns = [
    path('district/',views.home,name='home')
]