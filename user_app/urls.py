from django.urls import path



from .views import userdashboard

urlpatterns =[
    path('',userdashboard,name='userdashboard')
]