from django.urls import path
from . import views

urlpatterns = [
    path('', views.listMovies, name='listMovies'),
    path('<int:movie_id>', views.detailMovie, name='detailMovie'),
    path('addMovie/', views.addMovie, name='addMovie'),
    path('<int:movie_id>/delete/', views.deleteMovie, name='deleteMovie'),
    path('<int:movie_id>/edit/', views.editMovie, name='editMovie'),
]