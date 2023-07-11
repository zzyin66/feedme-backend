from django.db import models
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

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    reccomendations = models.ManyToManyField(Feed)

    def __str__(self):
        return self.username

