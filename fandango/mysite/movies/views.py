from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from . import models
from django.shortcuts import render, get_object_or_404

#home page
def home(request):
    return render(request, "movies/home.html", {
        'theaters': models.Theater.objects.all(),
        'movies': models.Movie.objects.all()
    })

#get json file
def get_json(request):
    return render(request, "https://raw.githubusercontent.com/aryaswanie/583-final/master/fandango/mysite/data.json", {
    })

#list of theaters
def listTheaters(request):
    theaters = models.Theater.objects.all()
    return render(request, "movies/listTheater.html", {
        "listType": "Theaters",
        "objects": theaters,
    })

#List of movies
def listMovies(request, movie_genre='', movie_genre1=''):
    movies = models.Movie.objects.all()
    if movie_genre == '':
        return render(request, "movies/listMovie.html", {
            "list_type": "Movies",
            "objects": movies,
        })
    elif movie_genre1 == '':
        return render(request, "movies/listMovie.html", {
            "list_type": "Movies",
            "objects": objects.filter(movie_genre__iexact=movie_genre),
        })
    else:
        return render(request, "movies/listMovie.html", {
            "list_type": "Movies",
            "objects": objects.filter(movie_genre__iexact=movie_genre+"/"+movie_genre1),
        })


#detail for movies
#thanks help from class!
def movieDetail(request, movie_id):
    movie = get_object_or_404(models.Movie, movie_id=movie_id)
    theaterObjects = movie.theaters.all()
    theaters = []
    for th, theater in enumerate(theaterObjects):
        theaters.append(theater.name)
    context = {
        'title' : movie.title,
        'poster' : "https://" + movie.poster,
        'theaters' : theaters,
        'theatername' : theater.name,
        'rating' : movie.rating,
        'runtime' : movie.runtime,
    }

    return render(request, "movies/movieDetail.html", context)

def theaterDetail(request, th_id):
      theater = get_object_or_404(models.Theater, th_id=th_id)
      movieObjects = theater.movie_set.all()
      context = {
        'name' : theater.name,
        'address' : theater.address,
        'phone' : theater.phone,
        'movies' : movieObjects,
      }
      return render(request, "movies/theaterDetail.html", context)

#api codes from class
def api(request, slug):

    if slug == 'movies':
        data = models.Movie.objects.values()
    elif slug == 'showtimes':
        data = models.Showtime.objects.values()
    else:
        data = models.Theater.objects.values()

    f_data = {"Data": [w for w in data]}

    return JsonResponse(f_data)
