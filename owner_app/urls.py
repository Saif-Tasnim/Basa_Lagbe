from django.urls import path
from .views import ownerDash,ownerBuy,ownerSell,ownerRent

urlpatterns = [
    path("", ownerDash, name="dash"),
    path("Owner-Buy",ownerBuy,name="buy"),
    path("Owner-Sell",ownerSell, name="sell"),
    path("Owner-Rent",ownerRent, name="rent")
   
]