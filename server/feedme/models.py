from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Feed(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.TextField()  
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    date = models.DateField()
    image = models.TextField()
    category = models.TextField()
    keywords = models.JSONField()
    
    class Meta:
        ordering = ["date"]
    
    def __str__(self):
        return self.title

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    feed_history = models.ManyToManyField(Feed, related_name="feed_history")
    recommendations = models.ManyToManyField(Feed, related_name="recommendations")
    keywords = models.JSONField(null=True, blank=True, default=dict)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
