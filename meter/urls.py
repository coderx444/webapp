from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meterdata', MeterDataViewSet)


urlpatterns = [
    path('',profile,name="profile"),
    path('home/',index,name='index'),
    path('totalbill/',TotalBill,name='totalbill'),
    path('api/meter/data',
         MeterDataListViewSet.as_view()),
    path('', include(router.urls)),
]