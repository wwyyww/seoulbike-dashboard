from django.db import models

class Station(models.Model):
    station_id = models.IntegerField(verbose_name='대여소 번호', unique=True)
    station_name = models.CharField(max_length=200, verbose_name='대여소명')
    location = models.CharField(max_length=200, verbose_name='자치구') 
    addr1 = models.CharField(max_length=200, verbose_name='주소1')
    addr2 = models.CharField(max_length=200, verbose_name='주소2', null=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=6, verbose_name='위도')
    longitude = models.DecimalField(max_digits=11, decimal_places=6, verbose_name='경도')

class Usage(models.Model):
    use_count = models.IntegerField(verbose_name='이용량')
    use_date = models.CharField(max_length=8,verbose_name='대여날짜')
    station_id = models.IntegerField(verbose_name='대여소 번호')
    gender = models.CharField(max_length=10, verbose_name='성별',null=True)
    age_range = models.CharField(max_length=10, verbose_name='연령대', null=True) 

class StationUsage(models.Model):
    district = models.CharField(max_length=255)
    station_name = models.CharField(max_length=255)
    use_ym = models.CharField(max_length=6)
    rental_count = models.IntegerField()
    return_count = models.IntegerField()