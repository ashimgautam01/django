from django.urls import path
from .views import *
urlpatterns = [
    path('',feedback_view,name="list"),
    path('show/<str:id>',show_workshop,name="show"),
    path('member',member_list,name="member"),
    path('feedback/',show_feedback,name="feed"),

]
