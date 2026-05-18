from django.urls import path
from .views import createActor, getActors, getActorById, updateActor, deleteActor

urlpatterns = [
    path('createActor/', createActor, name = 'createActor'),
    path('actors/', getActors, name = 'getAllActors'),
    path('actors/<int:id>/', getActorById, name = 'getActorsById'),
    path('updateActor/<int:id>/', updateActor, name = 'updateActor'),
    path('deleteActor/<int:id>/', deleteActor, name = 'deleteActor')
]