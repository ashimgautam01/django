from django.contrib import admin
from django.urls import path
from .views import index,about,contact


urlpatterns = [
    path("",index,name="homepage"),
    path("about",about,name="about"),
    path("contact",contact,name="contact")
]