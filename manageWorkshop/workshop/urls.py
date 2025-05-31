from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('feed/',feedback_view,name="list"),
    path('show/<str:id>',show_workshop,name="show"),
    path('member',member_list,name="member"),
    path('feedback/',show_feedback,name="feed"),
    path("",home,name="home"),
    path("accounts/profile/",profile , name="profile"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
