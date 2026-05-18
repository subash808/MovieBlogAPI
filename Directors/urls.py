from django.urls import path
from .views import createDirector, getDirectors, getDirectorById, updateDirector, deleteDirector

urlpatterns = [
    path('createDirector/', createDirector, name = 'create_director'),
    path('directors/', getDirectors, name = 'all_directors'),
    path('directors/<int:id>/', getDirectorById, name = 'director_by_id'),
    path('updateDirector/<int:id>/', updateDirector, name = 'update_director'),
    path('deleteDirector/<int:id>/', deleteDirector, name = 'delete_director')
]