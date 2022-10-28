from . import views
from django.urls import path

urlpatterns = [
    path('district/',views.home,name='home'),
    path('district/<str:region>/list',views.district,name='region')
]