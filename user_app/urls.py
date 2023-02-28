from django.urls import path



from .views import userDash,userBuy,userShow,userRent
urlpatterns =[
    path("", userDash, name="user-dash"),
    path("user-Buy",userBuy,name="user-buy"),
    path("user-show",userShow, name="user-show"),
    path("user-Rent",userRent, name="user-rent")
]