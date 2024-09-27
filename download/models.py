from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spotify_url = models.URLField()
    filename = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    downloaded = models.BooleanField(default=False)