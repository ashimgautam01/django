from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def create_post(request):
    return render(request,'addpost.html')

def get_all_post(request):
    return render(request,'getallpost.html')