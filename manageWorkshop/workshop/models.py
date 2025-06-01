from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.title
        return f"s{self.title}"


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    workshops = models.ManyToManyField(Workshop, blank=True)

    def __str__(self):
        return self.name
    

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return f"{self.name}"
    
class BaseTimestampModel(models.Model):
    created_At=models.DateTimeField( auto_now_add=True)
    updated_At=models.DateTimeField( auto_now_add=True)

    class Meta:
        abstract=True

class Post(BaseTimestampModel):
    title = models.CharField(max_length=200)
    content=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Comment(BaseTimestampModel):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    content=models.TextField()

    def __str__(self):
        return self.post.title
    