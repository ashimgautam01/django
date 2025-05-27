from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    data={
        "title":"Home Page"
    }
    return render(request,'homepage/home.html',data)


def about(request):
    data={
        "title":"About Page"
    }
    return render(request,'homepage/about.html',data)

def skills(request):
    data = {
        'skills': ['python', 'django', 'html', 'css']
    }
    return render(request,'homepage/skill.html',data)