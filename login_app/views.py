from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from register_app.models import RegularUser

# Create your views here.

def login_view(request) :
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        # user = authenticate(request, username=username, password=password)
        user = RegularUser.objects.get()
        if user is None :
            context = {"error" : "Invalid user email or password."}
            return render(request, 'login_page/login.html', context)
        else :
            login(request, user)
            return redirect("/")
    return render(request, 'login_page/login.html')