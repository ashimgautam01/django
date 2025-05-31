from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def workshop_list(request):
 
    context={
        "title":"WorkshopList",
        "workshop":Workshop.objects.all(),
        "members":Member.objects.all()
    }
    return render(request,'workshop/workshoplist.html',context)
  

def show_workshop(request,id):

    """
    .get()=> return single object
    .filter()=> return multiple object
    .all() => return all
    """
    context={
        "author":get_object_or_404(Workshop,id=id),
        "member":Member.objects.filter(workshops=id)
        # "author":Workshop.objects.get(id=id)  
    }
    return render(request,'workshop/workshop_details.html',context)

def member_list(request):
        context={
        "members":Member.objects.all()
        }
    
        return render(request,'workshop/memberlist.html',context)


def form(request):
     form=ContactForm(request.POST or None)
     if form.is_valid():
        print(form.cleaned_data)
        return render(request, 'workshop/thank.html')
     context={
          "form":form
     }
     return render(request,'workshop/forms.html',context)


def feedback_view(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return render(request, 'workshop/thank.html')
    return render(request, 'workshop/show.html', {'form': form})

def show_feedback(request):
    feeds=Feedback.objects.all()
    context={
          "form":feeds
     }
    return render(request, 'workshop/showall.html',context)

def home(request):
     return render(request,'workshop/showall.html')


@login_required(login_url="login")
def profile(request):
    # if not request.user.is_authenticated:
    #     return HttpResponse("Please login is first")
    
    context={
        'key':"34343453"
    }
    return render(request,'profile.html',context)