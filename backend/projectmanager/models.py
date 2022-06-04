from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import maskpass

class Project(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.title

class Project_Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    tools = models.TextField()
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class User(models.Model):
    # host = 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # planning idea create a encrypt and decrypt method for the password
    
    def __str__(self) -> str:
        return self.name