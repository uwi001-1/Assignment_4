from django.db import models
from user.models import CustomUser

# Create your models here.
class Task(models.Model):
    TYPE_CHOICE = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    duedate = models.DateField()
    status = models.CharField(max_length=20, choices=TYPE_CHOICE)

    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_to')

    created_date = models.DateTimeField(auto_now_add=True)
    updates_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title