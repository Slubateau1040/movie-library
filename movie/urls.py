from django.urls import path
from . import views

urlpatterns = [
    path('', views.listMovies, name='listMovies'),
    path('<int:movieId>', views.detailMovie, name='detailMovie'),
]