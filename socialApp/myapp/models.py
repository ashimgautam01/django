from django.db import models
# Create your models here.
    

class Post(models.Model):
    description = models.CharField(max_length=505)
    image = models.CharField(max_length=255,blank=True)
    user = models.ManyToManyField('User', related_name='posts')
    like = models.IntegerField(default=0)
    liked_by = models.ManyToManyField('User', related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    content=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    