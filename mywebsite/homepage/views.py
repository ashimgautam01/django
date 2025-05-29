from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def index(request):
   context={
       "name":"Ashim Gautam",
       "role":"Web Developer"
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

def project(request):
    # project_details={
    #      'portfolio': {
    #     'title': 'Portfolio Website',
    #     'description': 'Showcase your skills, resume, and projects with a personal touch.',
    #     'image': 'images/code.jpg'
    # },
    # 'blog': {
    #     'title': 'Blog Platform',
    #     'description': 'Build a fully functional blog with user login, post creation, and comments.',
    #     'image': 'images/html.jpg'
    # },
    # 'chat': {
    #     'title': 'Blog Platform',
    #     'description': 'Build a fully functional blog with user login, post creation, and comments.',
    #     'image': 'images/python.jpg'
    # },
    # 'Mental Health': {
    #     'title': 'Health Platform',
    #     'description': 'Build a fully functional Mental health with user login, post creation, and docotors appointments.',
    #     'image': 'images/react.jpg'
    # },

    # }
    project_details=Project.objects.all()
    
    return render(request,'homepage/project.html',{'project':project_details})

def skills(request):
    data = {
        'c': {
            "name": "C",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"
        },
        'cpp': {
            "name": "C++",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"
        },
        'python': {
            "name": "Python",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
        },
        'java': {
            "name": "Java",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"
        },
        'js': {
            "name": "JavaScript",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"
        },
        'react': {
            "name": "React",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"
        },
        'django': {
            "name": "Django",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"
        },
        'mongodb': {
            "name": "MongoDB",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"
        },
        'sql': {
            "name": "SQL",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"
        },
        'postgres': {
            "name": "PostgreSQL",
            "image": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"
        },
        'uiux': {
            "name": "UI/UX",
            "image": "https://img.icons8.com/color/96/figma.png"
        },
    }

    return render(request,'homepage/skill.html',{'skills':data})

def project_with_id(request,id):
    project=get_object_or_404(Project,id=id)

    return render(request,'homepage/single.html',{"project":project})