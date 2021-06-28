from .models import Station, LabResult
import csv


def load_stations():
	#Function to read stations.csv and load into database
	with open('water/data/stations.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
                    print(row)
                    # TODO: insert code to create Station objects from each row and save to database
