from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, TimeLog


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "password")

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return validated_data


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TimelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLog
        fields = ["project", "work_description", "status", "hours", 'date']

    def create(self, validated_data):
        validated_data["user"] = self.context.get("user")
        return super().create(validated_data)
