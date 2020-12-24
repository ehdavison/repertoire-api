from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    video = models.CharField(max_length=1000, null=True)
    tabs = models.CharField(max_length=1000, null=True)
    notes = models.CharField(max_length=20000, null=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'
