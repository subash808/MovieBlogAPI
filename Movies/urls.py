from django.urls import path
from .views import createMovie, getMovie, getMovies, updateMovie, deleteMovie

urlpatterns = [
    path('createMovie/', createMovie, name = 'create_movie'),
    path('movies/', getMovies, name = 'all_movies'),
    path('movie/<int:id>/', getMovie, name = 'movie_by_id'),
    path('updateMovie/<int:id>/', updateMovie, name = 'update_movie'),
    path('deleteMovie/<int:id>/', deleteMovie, name = 'delete_movie')
]