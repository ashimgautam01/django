from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    



class Department(models.Model):
    name=models.CharField()
    faculty=models.CharField()
    students=models.IntegerField(default=0)
    head=models.CharField()

    def __str__(self):
        return self.name
    








