from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context={
        "title":"Ashim",
        "heading":"Welcome to My Django Journey",
        "subhead":"Exploring the power of Django to build modern, secure, and scalable web applications.",
        "learn_approach":"My Django Learning Approach",
        "point_1":"Start with the official Django documentation and 10 days Workshop from CAPEC.",
        "point_2":"Build basic apps (blog, portfolio, to-do list) to understand the MVT structure",
        "point_3":"Explore Django admin, models, static, and templates.",
        "point_4":"Learn about user authentication,  views, and middleware.",
        "point_5":"Practice by deploying projects various platforms",
        "project_ideas":"Project Ideas",
        "pro_1":"portfolio",
        "pro_1_title":"Portfolio Website",
        "pro_1_desc":"Showcase your skills, resume, and projects with a personal touch",
        "pro_2":"blog",
        "pro_2_title":"Blog Platform",
        "pro_2_desc":"Build a fully functional blog with user login, post creation, and comments.",
        "pro_3":"task",
        "pro_3_title":"Task Manager",
        "pro_3_desc":"Allow users to register, log in, and manage personal tasks or notes.",
        "pro_4":"chat",
        "pro_4_title":"Chat App",
        "pro_4_desc":"Real-time communication using Django Channels and WebSockets."
    }
    return render(request,'homepage/home.html',context)

def about(request):
    context={
        "name":"Ashim Gautam",
        "description":"  Hi! I'm passionate about web development and Django. I love building beautiful and functional websites.",
        "location":"pokhara,Nepal",
        "role":"Student"
    }
    return render(request,'about/about.html',context)

def contact(request):
    return render(request,'contact/contact.html')

def project(request,project_name):
    project_details={
         'portfolio': {
        'title': 'Portfolio Website',
        'description': 'Showcase your skills, resume, and projects with a personal touch.',
        'image': 'images/ashim.png'
    },
    'blog': {
        'title': 'Blog Platform',
        'description': 'Build a fully functional blog with user login, post creation, and comments.',
        'image': 'images/html.jpg'
    },

    }
    project=project_details.get(project_name)
    if not project:
        return HttpResponse("<h1>NO project found </h1>")
    return render(request,'projects/projects.html',{'project':project})