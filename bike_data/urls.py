from django.urls import path
from .views import *

urlpatterns = [
    path('setup/', setup, name='setup'),
    path('setup_usage/', setup_usage),
    path('stations/', StationList.as_view(), name='station-list'),
    path('stations/<str:location>/', StationList.as_view()),
    path('usage/', UsageList.as_view()),
    path('setup_stationusage/<int:seq_no>/', setup_stationusage),
    path('stationusage/', StationUsageList.as_view()),
    path('chart/station_district/', station_by_district, name="stations_by_district"),
    path('chart/stationusage_analysis/', stationusage_analysis, name='stationusage_analysis'),
    path('map/',mapping, name='index'),
    path('seoulbike/',seoulbike, name='seoulbike'),
]
