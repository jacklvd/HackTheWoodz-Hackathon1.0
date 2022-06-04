from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=25)
    tools = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=False)