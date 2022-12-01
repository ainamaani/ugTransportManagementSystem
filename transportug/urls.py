from . import views
from django.urls import path

urlpatterns = [
    path('district/',views.home,name='home'),
    path('district/<str:region>/list',views.district,name='region'),
    path('company/<str:company>/list',views.company,name='company'),
    path('bus/shift/<int:id>',views.busShift,name='busShift'),
    path('bus/book/',views.bookShift,name='bookShift'),
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login')
]