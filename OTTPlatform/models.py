from django.db import models

# Create your models here.
class OTTPlatform(models.Model):
    ottName = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    launchYear = models.PositiveIntegerField(blank=True, null=True)
    ottLogo = models.ImageField(upload_to = 'ott/', blank = True, null = True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ottName