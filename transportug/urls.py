from . import views
from django.urls import path

urlpatterns = [
    path('district/',views.home,name='home'),
    path('district/<str:region>/list',views.district,name='region'),
    path('company/<str:company>/list',views.company,name='company'),
    path('bus/shift/<int:id>',views.busShift,name='busShift')
]