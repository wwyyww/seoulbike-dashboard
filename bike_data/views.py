import requests
from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from bike_data.serializers import *


API_KEY = settings.API_KEY


class StationList(generics.ListAPIView):
    serializer_class = StationSerializer

    def get_queryset(self, *args, **kwargs):
        param = self.kwargs.get('location')
        return Station.objects.filter(location=param)
        

@api_view(['GET'])
def setup(request):
    """
    이 함수는 데이터베이스에 초기 대여소 정보를 세팅하는 역할을 합니다.

    초기 데이터를 추가하려는 경우 이 함수를 호출하여 데이터베이스에 기본 데이터를 삽입할 수 있습니다.

    """
    for i in range(1, 3061, 500):
        url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/tbCycleStationInfo/{i}/{i+499}/"
        response = requests.get(url)
        data = response.json()['stationInfo']['row']
        serializer = StationSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

    return Response(len(serializer.validated_data), status=status.HTTP_200_OK)

class UsageList(generics.ListAPIView):
    serializer_class = UsageSerializer

    def get_queryset(self, *args, **kwargs):
        return Usage.objects.all()
        

@api_view(['GET'])
def setup_usage(request):
    # 기간 조정 필요
    start_year, end_year=2018,2023
    start_month,end_month=1,12
    for year in range(start_year, end_year+1):
        for month in range(start_month, end_month+1):
            ym = f"{year}{month:02d}"
            start = 1
            end = 1000
            while True:
                url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/tbCycleRentUseMonthInfo/{start}/{end}/{ym}"
                response = requests.get(url)
                data = response.json()['cycleRentUseMonthInfo']['row']
                serializer = UsageSerializer(data=data, many=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_REQUEST)
                if len(data)<1000:
                    break
                start+=1000
                end+=1000

    return Response(len(serializer.validated_data), status=status.HTTP_200_OK)
