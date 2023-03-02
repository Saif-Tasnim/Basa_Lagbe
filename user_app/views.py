from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import OwnerRent
from django.contrib import messages

# Create your views here.

# this "identifyUser" view identyfies whether the user is a land owner or a normal user.
# after identifying the user type it redirects the user to it's corresponding route.


def identifyUser(request):
    if request.user.is_authenticated:
        if request.user.is_land_owner:
            return redirect('/dashboard/owner-home')
        else:
            return redirect('/dashboard/user-home')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')

# belows views handles the normal user routes


def userDashboard(request):
    if request.user.is_authenticated:
        if not request.user.is_land_owner:
            return render(request, "TenantDashboard/user_base.html")
        else:
            return render(request, 'UserDashboard/unauthorized_user.html')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')


def userBuy(request):
    return render(request, "TenantDashboard/user_buy.html")


def userShow(request):
    return render(request, "TenantDashboard/user_sell.html")


def userRent(request):
    return render(request, "TenantDashboard/user_rent.html")


# belows views handles the property owners route

def ownerDashboard(request):
    if request.user.is_authenticated:
        if request.user.is_land_owner:
            return render(request, "OwnerDashboard/owner_base.html")
        else:
            return render(request, 'UserDashboard/unauthorized_user.html')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')


def ownerBuy(request):
    return render(request, "OwnerDashboard/owner_buy.html")


def ownerSell(request):
    if request.method == "POST":
        get_method = request.POST.copy()
        divission = get_method.get("divission")
        district = get_method.get("district")
        location = get_method.get("location")
        price = get_method.get("price")
        ammount = get_method.get("ammount")
        floors_count = get_method.get("floors_count")
        floor_face = get_method.get("floor_face")
        details = get_method.get("details")
        photo_url = get_method.get("photo_url")
        print(divission, district, location, price, ammount,
              floors_count, floor_face, details, photo_url)
    return render(request, "OwnerDashboard/owner_sell.html")


def ownerRent(request):
    if request.method == "POST":
        get_method = request.POST.copy()
        property_type = request.POST.get("property_type")
        rent_type = request.POST.get("rent_type")
        division = get_method.get("division")
        district = get_method.get("district")
        property_location = get_method.get("location")
        rent_money = get_method.get("money")
        money_type = get_method.get("money_type")
        floor_no = get_method.get("floor_no")

        floor_face = get_method.get("floor_face")
        plot_size = get_method.get("numerical_value_plot")
        numerical_value_type = get_method.get("numerical_value_type")
        area_description = get_method.get("details")
        rent_photo = get_method.get("rentimage")
        # print(property_type, rent_type, division, district, location, money, money_type, floor_no,
        #       floor_face, numerical_value_plot, numerical_value_type, details, photo_url)
        rent_data = OwnerRent(property_type=property_type, rent_type=rent_type, division=division, district=district, property_location=property_location, rent_money=rent_money, money_type=money_type,
                              floor_no=floor_no, floor_face=floor_face, plot_size=plot_size, numerical_value_type=numerical_value_type, area_description=area_description, rent_photo=rent_photo)
        rent_data.save()
        messages.success(request, "Your Rental Post added sucessfully!")

        return render(request, "OwnerDashboard/owner_rent.html")

    return render(request, "OwnerDashboard/owner_rent.html")
