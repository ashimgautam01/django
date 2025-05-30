from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    description=models.CharField()
    image=models.CharField()
    # user=
    like=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    content=models.CharField(max_length=50)
    # user= 
    # post=
    created_at=models.DateTimeField(auto_now=True)