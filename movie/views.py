from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def listMovies(request):
    genre_list = Movie.objects.values_list('genre', flat=True).distinct()
    genre_select = request.GET.get('genre')
    if genre_select:
        movies = Movie.objects.filter(genre=genre_select)
    else:
        movies = Movie.objects.all()
    context = {'movies': movies, 'genre_list': genre_list}
    return render(request, 'movie/listMovies.html', context)

def detailMovie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/detailMovie.html', {'movie': movie})

def addMovie(request):
    if request.method == 'POST':
        title = request.POST['title']
        genre = request.POST['genre'].capitalize()
        platform = request.POST['platform']
        is_finished = request.POST.get('is_finished', False) == 'on'
        rating = request.POST['rating']
        Movie.objects.create(title=title, genre=genre, platform=platform, is_finished=is_finished, rating=rating)
        return HttpResponseRedirect(reverse('listMovies'))
    else :
        return render(request, 'movie/addMovie.html')

def deleteMovie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return HttpResponseRedirect(reverse('listMovies'))

def editMovie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        title = request.POST['title']
        genre = request.POST['genre'].capitalize()
        platform = request.POST['platform']
        is_finished = request.POST.get('is_finished', False) == 'on'
        rating = request.POST['rating']
        movie.title = title
        movie.genre = genre
        movie.platform = platform
        movie.is_finished = is_finished
        movie.rating = rating
        movie.save()
        return HttpResponseRedirect(reverse('listMovies'))
    else :
        return render(request, 'movie/editMovie.html', {'movie': movie})
