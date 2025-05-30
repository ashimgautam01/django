from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image'] 
    
class CommentForm(forms.ModelForm):
    
    class Meta:
        model=Comment
        fields=["content", "user", "post"]