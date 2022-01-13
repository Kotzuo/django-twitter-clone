from accounts.models import User
from django.db import models


class Post(models.Model):
    message = models.CharField(max_length=280)
    media = models.URLField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['created_at']
