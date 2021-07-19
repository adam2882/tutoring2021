from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField

class Station(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	station_type = models.CharField(max_length=20)
	latitude = models.FloatField()
	longitude = models.FloatField()
	county = models.CharField(max_length=30)
	location = PointField(null=True)

class LabResult(models.Model): 
	station = models.ForeignKey(Station, on_delete=models.CASCADE)
	status = models.CharField(max_length=100)
	sample_code = models.CharField(max_length=20)
	date = models.DateField()
	depth = models.FloatField(null=True)
	depth_units = models.CharField(max_length=15)
	parameter = models.CharField(max_length=100)
	result = models.FloatField()
	reporting_limit = models.FloatField(null=True)
	units = models.CharField(max_length=20)
	method_name = models.CharField(max_length=100)


