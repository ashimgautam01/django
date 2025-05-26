from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("this is my home page")
    context={
        "homepage":"django day 2",
        "message":"welcome to day 2 of django workshop"
    }

    return render(request,'homepage/home.html',context)

def about(request):
    return HttpResponse("this is about page")

def contact(request):
    return HttpResponse("this is an contact page")          

