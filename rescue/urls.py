from django.urls import path
from .views import *

urlpatterns = [
    path('car_list/', CarList.as_view(), name='car_list'),
    path('second_car_list/', SecondCarList.as_view(), name='second_car_list'),
    path('car/', CarAPI.as_view(), name='car'),
    
]