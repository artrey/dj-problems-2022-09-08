from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

