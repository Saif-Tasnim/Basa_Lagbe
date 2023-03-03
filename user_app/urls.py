from django.urls import path

from .views import (identifyUser, ownerBuy, ownerDashboard, ownerRent,
                    ownerSell, userBuy, userDashboard, userRent, userShow)

urlpatterns =[
    path("", identifyUser, name="identify-user"),
    path("user-home", userDashboard, name="user-home"),
    path("user-buy",userBuy,name="user-buy"),
    path("user-show",userShow, name="user-show"),
    path("user-rent",userRent, name="user-rent"),
    path("owner-home", ownerDashboard, name="owner-home"),
    path("owner-buy",ownerBuy,name="buy"),
    path("owner-sell",ownerSell, name="sell"),
    path("owner-sell/<str:property_type>/", ownerSell, name="sell_property"),
    path("owner-rent",ownerRent, name="rent")
]