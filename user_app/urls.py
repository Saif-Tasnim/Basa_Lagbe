from django.urls import path

from .views import (identifyUser, ownerBuy, ownerDashboard, ownerRent,
                    ownerSell, userBuy, userDashboard, userRent, userShow,owner_post,delete_post,updatepost)

urlpatterns =[
    path("", identifyUser, name="identify-user"),
    path("user-home", userDashboard, name="user-home"),
    path("user-buy",userBuy,name="user-buy"),
    path("user-show",userShow, name="user-show"),
    path("user-rent",userRent, name="user-rent"),
    path("owner-home", ownerDashboard, name="owner-home"),
    path("owner-buy",ownerBuy,name="buy"),
    path("owner-sell",ownerSell, name="sell"),
    path("owner-rent",ownerRent, name="rent"),
    path("owner-post",owner_post, name="posts"),
    path("post_delete/<int:id>/",delete_post, name="deletepost"),
    path("update/<int:id>/",updatepost, name="updatepost")
]