from django.urls import path
from .views import *

urlpatterns = [
    path('student/',student_api,name="student"),
    path('depart/',department,name="depart")
]
