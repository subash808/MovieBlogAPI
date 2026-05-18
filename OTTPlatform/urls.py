from django.urls import path
from .views import createOTT, getOTTs, getOTTById, updateOTT, deleteOTT

urlpatterns = [
    path('createOTT/', createOTT, name = 'create_ott'),
    path('otts/', getOTTs, name = 'all_ott'),
    path('ott/<int:id>/', getOTTById, name = 'ott_by_id'),
    path('updateOTT/<int:id>/', updateOTT, name = 'update_ott'),
    path('deleteOTT/<int:id>/', deleteOTT, name = 'delete_ott')
]