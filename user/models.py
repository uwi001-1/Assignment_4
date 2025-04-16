from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.text import slugify 

# Create your models here.
class CustomUser(AbstractUser):
    CHOICES = (
        ('regular_user', 'Regular User'),
        ('admin', 'Admin'),
    )
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=255, unique=True)

    first_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    phone= models.CharField(max_length=15, null=True, default='')
    role = models.CharField(max_length=20, choices=CHOICES)

    created_date = models.DateTimeField(auto_now_add=True)
    updates_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name