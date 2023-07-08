from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    reccomendations = models.ManyToManyField(Feed)

    def __str__(self):
        return self.username


class Feed(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    content = models.TextField()  
    title = models.CharField()
    url = models.CharField()
    date = models.DateField()
    
    class Meta:
        ordering = ["date"]
    
    def __str__(self):
        return self.title

