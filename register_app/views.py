from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import RegularUser

# Create your views here.

def register(request) :
    if request.method == "POST" :
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if first_name and last_name and email and password :
            is_exist = RegularUser.objects.filter(email = email)
            if not is_exist :
                user_obj = RegularUser.objects.create(first_name = first_name, last_name = last_name, email= email, password = password)
                return render(request, 'register_page/user_created.html')
            else :
                return render(request, 'register_page/user_exist.html')
    return render(request,'register_page/register.html')