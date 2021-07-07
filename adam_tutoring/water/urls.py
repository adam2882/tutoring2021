from django.urls import path

from .views import StationsMapView
from . import views

app_name = "water"

urlpatterns = [
    path("map/", StationsMapView.as_view()),
    path('', views.index, name='index'),
    path('<int:station_id>/', views.station_details, name='station_details')
]