from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

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

