from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=1000, default="No description provided")
    image = models.CharField()
    technology = models.JSONField(default=list, blank=True)
    demo=models.URLField(default="")

    def __str__(self):
        return f"{self.title}"\
        

class Personal(models.Model):
    name=models.CharField( max_length=50)
    profile=models.CharField()
    email=models.EmailField()
    description=models.CharField(default="")
    location=models.CharField(default="")
    phone=models.CharField()
    role=models.CharField()
    domin=models.CharField()
    github=models.URLField(default="")
    linkden=models.URLField(default="")
    facebook=models.URLField(default="")
    portfolio=models.URLField(default="")

    def __str__(self):
        return f"{self.name}"
    
    