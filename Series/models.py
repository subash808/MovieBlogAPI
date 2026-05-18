from django.db import models
from actors.models import Actor
from Directors.models import Directors
from OTTPlatform.models import OTTPlatform


class Series(models.Model):
    seriesName = models.CharField(max_length = 150)

    hero = models.ForeignKey(
        Actor,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'hero_series'
    )

    director = models.ForeignKey(
        Directors,
        on_delete = models.SET_NULL,
        null = True,
        related_name = 'directed_series'
    )

    ottPlatform = models.ForeignKey(
        OTTPlatform,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'series'
    )

    cast = models.ManyToManyField(
        Actor,
        blank = True,
        related_name = 'cast_series'
    )

    seasons = models.PositiveIntegerField(default = 1)
    totalEpisodes = models.PositiveIntegerField(default = 1)

    musicDirector = models.CharField(max_length = 100, blank = True, null = True)
    producer = models.CharField(max_length = 100, blank = True, null = True)

    imdbRating = models.DecimalField(max_digits = 3, decimal_places = 1)
    reviews = models.TextField()

    releaseDate = models.DateField()
    genre = models.CharField(max_length = 100) 
    shortDescription = models.TextField()

    posterImage = models.ImageField(upload_to = 'series/posters/', blank = True, null = True)

    createdAt = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.seriesName