from django.db import models
from django.contrib import admin

# Model for Movie
class Movie(models.Model):
    Title = models.CharField(max_length=100)
    MovieID = models.IntegerField(primary_key=True)
    Rating = models.FloatField()
    ReleaseDate = models.DateField()
    DirectorEmail = models.EmailField()

# Admin configuration
class MovieAdmin(admin.ModelAdmin):
    list_display = ('Title', 'MovieID', 'Rating', 'ReleaseDate', 'DirectorEmail')
