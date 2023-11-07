from django.urls import path
from .views import *

urlpatterns = [
    path('stations/<str:location>/', StationList.as_view()),
]
