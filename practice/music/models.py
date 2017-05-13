from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=200)
	album_title = models.CharField(max_length=200)
	album_logo = models.CharField(max_length=200)
	genere = models.CharField(max_length=200)

	def __str__(self):
		return self.artist +'-'+ self.album_title

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=200)
	song_title = models.CharField(max_length=200)
	is_favorite= models.BooleanField(default=False)

	def __str__(self):
		return self.song_title