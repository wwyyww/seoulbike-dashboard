from django.db import models

class Station(models.Model):
    station_id = models.IntegerField(verbose_name='대여소 번호')
    station_name = models.CharField(max_length=200, verbose_name='대여소명')
    location = models.CharField(max_length=200, verbose_name='자치구') 
    addr1 = models.CharField(max_length=200, verbose_name='주소1')
    addr2 = models.CharField(max_length=200, verbose_name='주소2', null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='위도')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='경도')

class Usage(models.Model):
    station = models.ForeignKey(Station, related_name='usages', on_delete=models.CASCADE)
    use_count = models.IntegerField(verbose_name='이용량')
    use_date = models.DateField(verbose_name='대여날짜')