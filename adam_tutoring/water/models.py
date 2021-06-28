from django.db import models

class Station(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	station_type = models.CharField(max_length=20)
	latitude = models.FloatField()
	longitude = models.FloatField()
	county = models.CharField(max_length=30)

class LabResult(models.Model): 
	station = models.ForeignKey(Station, on_delete=models.CASCADE)
	status = models.CharField(max_length=40)
	sample_code = models.CharField(max_length=20)
	date = models.DateField()
	depth = models.FloatField()
	depth_units = models.CharField(max_length=15)
	parameter = models.CharField(max_length=40)
	result = models.FloatField()
	reporting_limit = models.FloatField()
	units = models.CharField(max_length=20)
	method_name = models.CharField(max_length=40)
