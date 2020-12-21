from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    video = models.CharField(max_length=1000, null=True)
    tabs = models.CharField(max_length=1000, null=True)
    notes = models.CharField(max_length=20000, null=True)
    user_id = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title}'
