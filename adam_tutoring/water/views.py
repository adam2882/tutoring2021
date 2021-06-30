from django.shortcuts import render
from django.http import HttpResponse
from .models import Station

def index(request):
    station_results = Station.objects.all()
    station_table = '<table><tr><th>Name</th><th>Latitude</th><th>Longitude</th><th>County</th></tr>'
    for station in station_results:
        station_table += '<tr><td>'
        station_table += '</td><td>'.join([station.name, str(station.latitude), str(station.longitude), station.county])
        station_table += '</td></tr>'
    station_table += '</table>'
    return HttpResponse(station_table)
