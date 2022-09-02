from django.contrib import admin

from .models import Project, TimeLog

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "created_at", "updated_at"]


@admin.register(TimeLog)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "project", "work_description", "status", "hours"]
