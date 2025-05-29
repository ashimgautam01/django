from django.urls import path
from .views import *
urlpatterns = [
    path('',workshop_list,name="list"),
    path('show/<str:id>',show_workshop,name="show"),
    path('member',member_list,name="member"),
]
