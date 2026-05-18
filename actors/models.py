from django.db import models

class Actor(models.Model):

    actorName = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    designations = models.CharField(max_length = 300)
    noOfMovies = models.PositiveIntegerField()
    debutMovies = models.CharField(max_length = 100)
    latestMovie = models.CharField(max_length = 100)
    upcomingMovie = models.CharField(max_length = 100, blank = True, null = True)
    surname = models.CharField(max_length = 50)
    shortDescription = models.CharField(max_length = 300)
    noOfHits = models.PositiveIntegerField()
    blockBusters = models.PositiveIntegerField()
    averageMovies = models.PositiveIntegerField()
    since = models.PositiveIntegerField()
    awards = models.TextField()
    actorImage = models.ImageField(upload_to = 'actors/', blank = True, null = True)
    createdAt = models.DateTimeField(auto_now_add = True)

    def __str__(self): 
        return self.actorName