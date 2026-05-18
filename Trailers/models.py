from django.db import models
from Movies.models import Movies
from Directors.models import Directors
from actors.models import Actor


class Trailer(models.Model):
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name='trailers'
    )

    youtubeLink = models.URLField()
    description = models.TextField()

    releaseDate = models.DateField()

    leadActors = models.ManyToManyField(
        Actor,
        blank=True,
        related_name='trailers'
    )

    director = models.ForeignKey(
        Directors,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='trailers'
    )

    musicDirector = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)

    thumbnailImage = models.ImageField(
        upload_to='trailers/',
        blank=True,
        null=True
    )

    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie.movieName