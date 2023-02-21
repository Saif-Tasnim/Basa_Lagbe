from django.urls import path
from .views import ownerDash

urlpatterns = [
    path("", ownerDash, name="dash")
   
]