from dataclasses import field
from rest_framework import serializers
from projectmanager.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'