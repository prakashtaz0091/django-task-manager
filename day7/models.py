from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    status_choices = [
        ('NI','Not Started'),
        ('IP','In Progress'),
        ('CM','Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    desc = models.TextField()
    deadline = models.DateField(auto_now_add=False)
    status = models.CharField(choices = status_choices, max_length=2, default="NI" )


    def __str__(self):
        return self.title
    