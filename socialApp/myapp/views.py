from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from .models import *

def home(request):
    return render(request,'home.html')

def create_post(request):
    form = PostForm(request.POST or None)
    print(request)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('getall')
        else:
            message = "Failed to create post"
            return render(request, 'addpost.html', {'form': form, 'message': message, 'errors': form.errors})
    return render(request, 'addpost.html', {'form': form})

def get_all_post(request):
    post_Data=Post.objects.all().order_by("-created_at")
    context={
        "post":post_Data
    }
    return render(request,'getallpost.html',context)

def comment_post(request,id):
    comment=CommentForm(request.POST)
    print(comment)
    if comment.is_valid():
        comment.post=id
        comment.save()
        print("Valid")
        return redirect('getall')
    print("no valid")
    return redirect('getall')
    
def get_comment(request, id):
    comments = Comment.objects.filter(post=id)
    # Display comments as plain text for now since comments.html does not exist
    print(comments)
    return render(request, 'home.html', {'comments': comments})

def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.like += 1
    post.save()
    print(post)
    return redirect('getall')   

def get_profile(request):
    return render(request,'profile.html')