from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    tools = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
