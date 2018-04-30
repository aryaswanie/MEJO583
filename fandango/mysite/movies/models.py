from django.db import models

# adapting codes from class 17
#thanks for help from class
class Theater(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    lat = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    long = models.DecimalField(max_digits=100,decimal_places=2,null=True)
    th_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100,null=True)
    theaters = models.ManyToManyField(Theater)
    movie_id = models.IntegerField(unique=True)
    runtime = models.IntegerField()
    releaseDate = models.DateField()
    poster = models.CharField(max_length=100,null=True)
    rating = models.CharField(max_length=100,null=True)
    movie_genre = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, default="")
    time = models.CharField(max_length = 100)

    def __str__(self):
        return self.movie.title + self.theater.name + self.time
