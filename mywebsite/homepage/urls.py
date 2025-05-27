
from django.urls import path
from .views import index,about,contact,project


urlpatterns = [
    path("",index,name="homepage"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("projects/<str:project_name>/",project,name="project")
]