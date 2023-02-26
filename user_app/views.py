from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def userDash(request):
    return render (request, "TenantDashboard/user_base.html")

def userBuy(request):
    return render (request,"TenantDashboard/user_buy.html")

def userShow(request):
    return render(request,"TenantDashboard/user_sell.html")


def userRent(request):
    return render(request, "TenantDashboard/user_rent.html")