from django.urls import path

from .views import index,about


urlpatterns = [
    path("", index, name="index"),
    path("aboutus", about, name="about")
]
