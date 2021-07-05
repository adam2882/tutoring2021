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


def float_helper(input_string):
	if input_string == '':
		return
	else:
		return(float(input_string))

def convert_date_helper(datetime_string):
	# Changes datetime of format 05/03/1967 09:00 and returns date in YYYY-MM-DD format
	date = datetime_string.split()[0]
	date_parts = date.split('/')
	return(date_parts[2] + '-' + date_parts[0] + '-' + date_parts[1])


def load_lab_results():
	with open('water/data/lab-results.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for counter, row in enumerate(reader):
			if counter % 10000 == 0:
				print(counter)
			try:
				station = Station.objects.get(pk=int(row['STATION_ID']))
			except Station.DoesNotExist:
				print(row)
				print('Station not found in database')
			else:
				if row['RESULT'] != '':
					# Only add entries that actually have a result
					# Depth allowed to be missing, all other fields are required
					result = LabResult(
						station=station,
						status=row['STATUS'],
						sample_code=row['SAMPLE_CODE'],
						date=convert_date_helper(row['SAMPLE_DATE']),
						depth=float_helper(row['SAMPLE_DEPTH']),
						depth_units=row['SAMPLE_DEPTH_UNITS'],
						parameter=row['PARAMETER'],
						result=row['RESULT'],
						reporting_limit=float_helper(row['REPORTING_LIMIT']),
						units=row['UNITS'],
						method_name=row['METHOD_NAME']
						)
					result.save()

