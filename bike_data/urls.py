from django.urls import path
from .views import *

urlpatterns = [
    path('setup/', setup, name='setup'),
    path('setup_usage/', setup_usage),
    path('stations/<str:location>/', StationList.as_view()),
    path('usage/', UsageList.as_view()),
    path('map/',mapping, name='index'),
    path('text/',text, name='practice'),
    path('seoulbike/',seoulbike, name='seoulbike'),
]
