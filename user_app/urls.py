from django.urls import path

from .views import (delete_post, deletesellflat, deletesellland, flatDetails,
                    identifyUser, owner_post, ownerBuy, ownerDashboard,
                    ownerRent, ownerSell, updatepost, userAccount, userBuy,
                    userDashboard, userRent, userSearch, userShow)

urlpatterns =[
    path("", identifyUser, name="identify-user"),
    path("account", userAccount, name="account"),
    path("user-home", userDashboard, name="user-home"),
    path("user-buy",userBuy,name="user-buy"),
    path("user-show",userShow, name="user-show"),
    path("user-rent",userRent, name="user-rent"),
    path("owner-home", ownerDashboard, name="owner-home"),
    path("owner-buy",ownerBuy,name="buy"),
    path("owner-sell",ownerSell, name="sell"),
    path("owner-sell/<str:property_type>/", ownerSell, name="sell_property"),
    path("owner-rent",ownerRent, name="rent"),
    path("owner-rent",ownerRent, name="rent"),
    path("owner-post",owner_post, name="posts"),
    path("post_delete/<int:id>/",delete_post, name="deletepost"),
    path("update/<int:id>/",updatepost, name="updatepost"),
    # path("", userDash, name="dash"),
    # path("user-Buy",userBuy, name="buy"),
    # path("user-Sell",userShow, name="sell"),
    # path("user-Rent",userRent, name="rent"),
    path("search",userSearch, name="search"),
    path("search/details",flatDetails, name="details"),
    path("deletesellflat/<int:id>/",deletesellflat, name="deletesellflat"),

    path("deletesellland/<int:id>/",deletesellland, name="deletesellland"),

]