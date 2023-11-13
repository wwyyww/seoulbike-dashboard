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
    station = models.ForeignKey(Station, related_name='usages', on_delete=models.CASCADE, db_column="station_id")
    use_count = models.IntegerField(verbose_name='이용량')
    use_date = models.CharField(max_length=8,verbose_name='대여날짜')
    gender = models.CharField(max_length=10, verbose_name='성별',null=True)
    age_range = models.CharField(max_length=10, verbose_name='연령대', null=True) 
