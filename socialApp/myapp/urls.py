from django.urls import path
from .views import *

urlpatterns = [
    path("",home ,name="home"),
    path("create/",create_post ,name="create"),
    path("getall/",get_all_post ,name="getall"),

]
