from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Video(models.Model):
    movie_id = models.CharField("MovieID", max_length=20, unique=True)
    movie_title = models.CharField("MovieTitle", max_length=200)
    actor1_name = models.CharField("Actor1Name", max_length=100)
    actor2_name = models.CharField("Actor2Name", max_length=100, blank=True)
    director_name = models.CharField("DirectorName", max_length=100)
    movie_genre = models.CharField("MovieGenre", max_length=50)
    release_year = models.PositiveIntegerField(
        "ReleaseYear",
        validators=[MinValueValidator(1888), MaxValueValidator(date.today().year + 1)]
    )

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"
