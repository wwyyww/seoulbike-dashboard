from django.urls import path
from .views import *

urlpatterns = [
    path('setup/', setup, name='setup'),
    path('setup_usage/', setup_usage),
    path('stations/<str:location>/', StationList.as_view()),
    path('usage/', UsageList.as_view()),
    path('setup_stationusage/<int:seq_no>/', setup_stationusage),
    path('stationusage/', StationUsageList.as_view())
]
