from django.db import models
from actors.models import Actor
from Directors.models import Directors
from OTTPlatform.models import OTTPlatform

# Create your models here.

class Movies(models.Model):

    movieName = models.CharField(max_length = 150)

    hero = models.ForeignKey(
        Actor,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'hero_movies'
    )

    director = models.ForeignKey(
        Directors,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'director_movies'
    )

    ott = models.ForeignKey(
        OTTPlatform,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'movies'
    )

    cast = models.ManyToManyField(
        Actor,
        blank = True,
        related_name = 'cast_movies'
    )

    musicDirector = models.CharField(max_length = 100)
    producer = models.CharField(max_length = 100)
    distributor = models.CharField(max_length = 100)

    satelliteRightsOwnedBy = models.CharField(max_length = 100)
    imdbRating = models.DecimalField(max_digits = 3, decimal_places = 1)

    reviews = models.TextField()
    releaseDate = models.DateField()
    genre = models.CharField(max_length = 100)
    shortDescription = models.TextField()

    posterImage = models.ImageField(upload_to = 'movies/posters/', blank = True, null = True)

    createdAt = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.movieName