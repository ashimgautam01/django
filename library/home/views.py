from django.shortcuts import render,get_object_or_404
from .models import *

def authors(request):
    data=Author.objects.all()
    print(data)
    return render(request,'authors.html',{'data':data})

def home(request):
    return render(request,'home.html')

def Books_page(request):
    data=Books.objects.all()
    return render(request,'books.html',{'book':data})


def single_Book(request,id):    
    book=get_object_or_404(Books,id=id)
    return render(request,'singleBook.html',{'book':book})

def single_Author(request,id):
    author = get_object_or_404(Author,id=id)
    
    return render(request, 'singleAuthor.html',{'author':author})