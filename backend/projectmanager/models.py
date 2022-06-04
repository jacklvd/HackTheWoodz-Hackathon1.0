from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    tools = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    # host = 
    user = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)