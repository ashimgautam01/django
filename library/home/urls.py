from django.urls import path
from .views import *

urlpatterns = [
    path('', home ,name="home"),
    path('authors', authors ,name="authors"),
    path('books', Books_page ,name="books"),
    path('singlebook/<int:id>', single_Book ,name="authors"),
    path('singleauthor/<str:id>', single_Author ,name="authors"),

]
