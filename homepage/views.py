from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("this is my home page")

def about(request):
    return HttpResponse("this is about page")

def contact(request):
    return HttpResponse("this is an contact page")