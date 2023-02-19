from django.shortcuts import render

# Create your views here.

def ownerDash(request):
    return render (request, "OwnerDashboard/owner_base.html")
