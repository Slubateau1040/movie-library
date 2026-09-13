from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def listMovies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie/listMovies.html', context)

def detailMovie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/detailMovie.html', {'movie': movie})