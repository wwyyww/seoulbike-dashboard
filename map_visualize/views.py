from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json

from django.http import HttpResponse

def index(request):
    return render(request, 'map_visualize/index.html')
# Create your views here.