from django.db import models
from django.utils import timezone
# Create your models here.


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    upload_time = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.song_name



class Podcast(models.Model):


    id = models.AutoField(primary_key=True)
    podcast_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=1100,blank=True, default='')
    upload_time = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.podcast_name



class Audiobook(models.Model):
    id = models.AutoField(primary_key=True)
    audiobook_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    upload_time = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.audiobook_name
