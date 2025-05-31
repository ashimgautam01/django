from django.urls import path
from .views import *

urlpatterns = [
    path("",home ,name="home"),
    path("create/",create_post ,name="create"),
    path("getall/",get_all_post ,name="getall"),
    path('like/<int:id>/', like_post, name='like'),
    path('add_comment/<int:id>/', comment_post, name='add_comment'),
    path('get_comment/<int:id>/', get_comment, name='get_comment'),

]
