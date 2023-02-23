from django.shortcuts import render

# Create your views here.

def ownerDash(request):
    return render (request, "OwnerDashboard/owner_base.html")

def ownerBuy(request):
    return render (request,"OwnerDashboard/owner_buy.html")

def ownerSell(request):
    return render(request,"OwnerDashboard/owner_sell.html")