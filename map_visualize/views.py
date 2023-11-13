from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import List_station, List_usage
import requests, json

from django.http import HttpResponse

def index(request):
    return render(request, 'map_visualize/index.html')
# Create your views here.

def prac(request):
    station_content = List_station.objects.all()
    usage_content = List_usage.objects.all()
    str = ''
    for usage in usage_content:
        str += "<p>번호. {} 누적사용량 {}</p><br>".format(usage.station_id, usage.use_count)
    return HttpResponse(str)