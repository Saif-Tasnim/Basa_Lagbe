from django.urls import path

from .views import index,about,contact,featured


urlpatterns = [
    path("", index, name="index"),
    path("aboutus", about, name="about"),
    path("contactus", contact, name="contact"),
    path("featured", featured, name="featured"),
]

