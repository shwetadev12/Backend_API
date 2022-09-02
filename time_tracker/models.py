from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    user = models.ManyToManyField(User, through="Timelog")
    title = models.CharField(max_length=56)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimeLog(models.Model):
    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress"
        DONE = "done"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    work_description = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices)
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)
