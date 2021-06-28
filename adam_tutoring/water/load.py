from .models import Station, LabResult
import csv


def load_stations():
	#Function to read stations.csv and load into database
	with open('water/data/stations.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['LATITUDE'] == '' or row['LONGITUDE'] == '':
				print(row)
			else:
				station = Station(
					id=row['STATION_ID'], 
					name=row['STATION_NAME'], 
					station_type=row['STATION_TYPE'], 
					latitude=row['LATITUDE'], 
					longitude=row['LONGITUDE'], 
					county=row['COUNTY_NAME'])
				station.save()