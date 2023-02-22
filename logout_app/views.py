from django.contrib.auth import logout
from django.shortcuts import redirect, render

# Create your views here.

def logout_view(request) :
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "logout_page/logout.html", {})
