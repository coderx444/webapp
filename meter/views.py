from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from authy.models import *
from rest_framework import viewsets, generics
from .serializer import MeterDataSerializer, MeterDataListSerializer
from django.db.models.functions import Coalesce
from django.db.models import Sum, Value as V
# Create your views here.


def index(request):
    return render(request,'index.html')

class MeterDataViewSet(viewsets.ModelViewSet):
    queryset = MeterData.objects.all()
    serializer_class = MeterDataSerializer


class MeterDataListViewSet(generics.ListAPIView):
    serializer_class = MeterDataListSerializer

    def get_queryset(self):
        user = self.request.GET.get("user_id")
        data =  Profile.objects.filter(user=user)
        return data



def profile(request):
    user =request.user
    profile_user = Profile.objects.get(user=user)
    meterData = MeterData.objects.filter(user=request.user).all()
    bill_data = Bill.objects.filter(meter_id= profile_user)
    context = {
        "meterData": meterData,
        "total_bill": bill_data,
        'profile_user': profile_user
    }
    return  render(request, 'profile.html', context)


def TotalBill(request):
    user = request.user
    profile_user = Profile.objects.get(user=user)
    if request.method == 'POST':
        total_bill = MeterData.objects.filter(user=request.user).aggregate(
            usage_of_unit=Coalesce(Sum('usage_of_unit'), V(0)))
        bill = Bill(meter_id=profile_user,
                    total_bill=total_bill['usage_of_unit']*10)
        bill.save()
        return redirect('profile')
    return render(request, 'profile.html')