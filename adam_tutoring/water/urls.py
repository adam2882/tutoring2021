from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:station_id>/', views.station_details, name='station_details')
]