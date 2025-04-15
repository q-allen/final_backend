from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    duration = models.CharField(max_length=50)
    genre = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            return round(sum(r.score for r in ratings) / ratings.count(), 1)
        return None

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = ('user', 'movie')  # One rating per user per movie

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}: {self.score}'

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.username} on {self.movie.title}"
