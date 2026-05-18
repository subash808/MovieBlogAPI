from django.urls import path
from .views import createSeries, getSeries, getSeriesList, updateSeries, deleteSeries

urlpatterns = [
    path('createSeries/', createSeries, name = 'create_series'),
    path('series/', getSeriesList, name = 'all_series'),
    path('series/<int:id>/', getSeries, name = 'series_by_id'),
    path('updateSeries/<int:id>/', updateSeries, name = 'update_series'),
    path('deleteSeries/<int:id>/', deleteSeries, name = 'delete_series')
]