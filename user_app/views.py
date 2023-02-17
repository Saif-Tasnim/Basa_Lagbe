from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def userdashboard(request):
  return  render(request,'UserDashboard/userdashboard.html')