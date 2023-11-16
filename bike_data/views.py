import requests
from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from bike_data.serializers import *
from io import StringIO
import chardet
import csv
from .show_chart import *
from django.http import JsonResponse 

API_KEY = settings.API_KEY

def station_by_district(request):
    image_base64 = barplot_station_per_district()
    return JsonResponse({'image_base64': image_base64})

def stationusage_analysis(request):
    if request.method == 'POST':
        district_param = request.POST.get('district_param', '')
        use_ym_param = request.POST.get('use_ym_param', '')
        version = int(request.POST.get('version', '1'))

        image_base64 = applyAnalysis(district_param, use_ym_param, version)
        return JsonResponse({'image_base64': image_base64})

    return render(request, 'bike_data/chart_analysis.html')

class StationList(generics.ListAPIView):
    serializer_class = StationSerializer

    def get_queryset(self, *args, **kwargs):
        param = self.kwargs.get('location')
        if param:
            return Station.objects.filter(location=param)
        else:
            return Station.objects.all()        


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
        serializer = StationAPISerializer(data=data, many=True)
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
    url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/tbCycleRentUseMonthInfo/1/5/202208"
    response = requests.get(url)
    data = response.json()['cycleRentUseMonthInfo']['row']
    serializer = UsageAPISerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StationUsageList(generics.ListAPIView):
    serializer_class = StationUsageSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self, *args, **kwargs):
        district_param = self.request.query_params.get('district', None)
        use_ym_param = self.request.query_params.get('use_ym', None)

        filters = {}

        if district_param:
            filters['district'] = district_param

        if use_ym_param:
            filters['use_ym'] = use_ym_param

        return StationUsage.objects.filter(**filters)

@api_view(['GET'])
def setup_stationusage(request, seq_no):
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
    file_url = "https://datafile.seoul.go.kr/bigfile/iot/inf/nio_download.do?&useCache=false"

    params = {
        'infId': 'OA-15249',
        'seqNo': seq_no,
        'seq': seq_no,
        'infSeq': '1',
    }

    response = requests.get(file_url, params=params, verify=False)

    if response.status_code == 200:
        content = response.content.decode('cp949')

        encoding_info = chardet.detect(response.content)
        encoding = encoding_info['encoding']
        content = response.content.decode(encoding)

        csv_file = StringIO(content)
        csv_reader = csv.reader(csv_file, delimiter=',')

        header = next(csv_reader)
        data = [dict(zip(header, row)) for row in csv_reader]
        
        for row_data in data:
            serializer = StationUsageSerializer(data=row_data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(row_data)

        return Response(len(data), status=status.HTTP_200_OK)
    else:
        return render(request, 'error.html', {'error_message': 'Failed'})

def mapping(request):
    return render(request, 'bike_data/index.html')

def seoulbike(request):
    #stationlist = Station.objects.all()
    #station_content = json.dumps(stationlist)
    #usagelist = Usage.objects.all()
    #usage_content = json.dumps(usagelist)
    station_content = Station.objects.all()
    usage_content = Usage.objects.all()
    content = {'station_content' : station_content, 'usage_content' : usage_content}
    return render(request, 'bike_data/seoulbike.html', content)