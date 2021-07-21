from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Station
from django.views.generic.base import TemplateView
import json
from django.core.serializers import serialize
from django.db.models import Count

def index(request):
    station_results = Station.objects.all()
    template = loader.get_template('water/index.html')
    context = {
        'station_results': station_results,
    }
    """station_table = '<table><tr><th>Name</th><th>Latitude</th><th>Longitude</th><th>County</th></tr>'
    for station in station_results:
        station_table += '<tr><td>'
        station_table += '</td><td>'.join([station.name, str(station.latitude), str(station.longitude), station.county])
        station_table += '</td></tr>'
    station_table += '</table>'
    return HttpResponse(station_table)"""
    return HttpResponse(template.render(context, request))
def station_details(request, station_id):
    station = Station.objects.get(pk=station_id)
    return HttpResponse(station.name)

class StationsMapView(TemplateView):
    template_name = "map.html"
    def get_context_data(self, **kwargs):
        top_stations = Station.objects.annotate(c=Count('labresult')).filter(c__gt=1000)
        context = super().get_context_data(**kwargs)
        context["stations"] = json.loads(serialize("geojson", Station.objects.all()))
        return context

