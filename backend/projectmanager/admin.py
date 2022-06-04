from django.contrib import admin

# Register your models here.
from .models import Project, User

admin.site.register(Project)