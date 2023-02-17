from django.urls import path



from .views import userdashboard

urlpatterns =[
    path('dashboard',userdashboard,name='userdashboard')
]