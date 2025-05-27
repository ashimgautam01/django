
from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="homepage"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("project/",project,name="project"),
    path("skills/",skills,name="skills")
]