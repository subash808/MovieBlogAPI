from django.db import models

# Create your models here.

class Directors(models.Model):

    directorName = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    designations = models.CharField(max_length = 100)
    noOfMovies = models.PositiveIntegerField()
    debutMovie = models.CharField(max_length = 100)
    latestMovie = models.CharField(max_length = 100)
    upcomingMovie = models.CharField(max_length = 100)
    hits = models.PositiveIntegerField()
    blockbusters = models.PositiveIntegerField()
    averageMovies = models.PositiveIntegerField()
    shortDescription = models.TextField()
    since = models.PositiveIntegerField()
    awards = models.CharField(max_length = 100)
    directorImage = models.ImageField(upload_to = 'directors/', blank = True, null = True)
    createdAt = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.directorName