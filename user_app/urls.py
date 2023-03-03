from django.urls import path



from .views import flatDetails, userDash,userBuy, userSearch,userShow,userRent
urlpatterns =[
    path("", userDash, name="dash"),
    path("user-Buy",userBuy,name="buy"),
    path("user-Sell",userShow, name="sell"),
    path("user-Rent",userRent, name="rent"),
    path("search",userSearch, name="search"),
    path("search/details",flatDetails, name="details")
]