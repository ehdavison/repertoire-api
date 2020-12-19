from django.db import models

# Create your models here.


class Song(models.Models):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    video = models.CharField(max_length=1000)
    tabs = models.CharField(max_length=1000)
    notes = models.CharField(max_length=20000)

    def __str__(self):
        return f'{self.title}'
