from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField()
    location = models.CharField()
    isVerified = models.BooleanField()
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"
    

class Books(models.Model):
    name=models.CharField(max_length=50)
    edition=models.CharField( max_length=50)
    description=models.CharField( max_length=50)
    published_year=models.DateField( auto_now=False, auto_now_add=False)
    page=models.IntegerField()
    author=models.ManyToManyField(Author,blank=True)

    def __str__(self):
        return f"{self.name}"
    


