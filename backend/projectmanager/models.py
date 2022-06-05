from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
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
    
    # planning idea to create encrypt and decrypt methods for the password
    
    def __str__(self) -> str:
        return self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
for user in User.objects.all():
    Token.objects.get_or_create(user=user)