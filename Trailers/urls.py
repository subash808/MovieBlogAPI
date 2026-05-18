from django.urls import path
from .views import createTrailer, getTrailer, getTrailers, updateTrailer, deleteTrailer

urlpatterns = [
    path('createTrailer/', createTrailer, name='create_trailer'),
    path('trailers/', getTrailers, name='all_trailers'),
    path('trailer/<int:id>/', getTrailer, name='trailer_by_id'),
    path('updateTrailer/<int:id>/', updateTrailer, name='update_trailer'),
    path('deleteTrailer/<int:id>/', deleteTrailer, name='delete_trailer'),
]