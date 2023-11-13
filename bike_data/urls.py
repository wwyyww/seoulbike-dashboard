from django.urls import path
from .views import *

urlpatterns = [
    path('setup/', setup, name='setup'),
    path('setup_usage/', setup_usage),
    path('stations/', StationList.as_view(), name='station-list'),
    path('stations/<str:location>/', StationList.as_view(), name='station-list-location'),
    path('usage/', UsageList.as_view()),

]
