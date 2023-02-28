from django.urls import path



from .views import userDash,userBuy,userShow,userRent
urlpatterns =[
    path("", userDash, name="dash"),
    path("user-Buy",userBuy,name="buy"),
    path("user-Sell",userShow, name="sell"),
    path("user-Rent",userRent, name="rent")
]