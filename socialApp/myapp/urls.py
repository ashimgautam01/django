from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("",home ,name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("accounts/profile/",get_profile , name="profile"),
    path("create/",create_post ,name="create"),
    path("getall/",get_all_post ,name="getall"),
    path('like/<int:id>/', like_post, name='like'),
    path('add_comment/<int:id>/', comment_post, name='add_comment'),
    path('get_comment/<int:id>/', get_comment, name='get_comment'),

]


