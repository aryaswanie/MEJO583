from django.urls import path
from . import views

#code from class 17
app_name='movies'
urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.listMovies, name='moviesList'),
    path('movies/<int:movie_id>/', views.movieDetail, name="movieDetails"),
    path('theaters/', views.listTheaters, name='theatersList'),
    path('theaters/<slug:th_id>/', views.theaterDetail, name="theaterDetails"),
    path('api/<slug:slug>/', views.api, name='api'),
]
