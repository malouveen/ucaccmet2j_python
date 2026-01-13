#Import necesarry packages
import json

# Opening and reading the files
with open('precipitation.json') as file:                                # Opening the precipitation data file 
    precipitation_data = json.load(file)   

with open('stations.csv') as file:                                      # Opening the stations csv file
    first_line = file.readline()
    stations = file.readlines()  

# Creating a dictionary from stations csv data
stations_data = {}
for lines in stations:
    location, state, station = lines.split(',')
    stations_data[location] = {'station': station.strip(), 'state':state}
print(stations_data)

# Calculating for each location
for location in stations_data:
    location_dictionary = stations_data[location]
    station = location_dictionary['station']
    state = location_dictionary['state']

    # 1.2 Selecting the measurements belonging to specific location data
    location_precipitation = []
    
    for measurement in precipitation_data:
        if measurement['station'] == station:
            location_precipitation.append(measurement)
    
    # 1.3 Total monthly precipitation
    location_monthly_precipitation = {}
    
    for measurement in location_precipitation:
        year, month, day = measurement['date'].split('-') 
        if month not in location_monthly_precipitation:
            monthly_precipitation = 0
        monthly_precipitation += measurement['value']
        location_monthly_precipitation[month] = monthly_precipitation
    list_precipitation_monthly = list(location_monthly_precipitation.values())
    print(f'Monthy Precipitation: {list_precipitation_monthly}')

    # 2.1 Total yearly precipitation
    yearly_precipitation = 0

    for month in location_monthly_precipitation:
        precipitation_per_month = location_monthly_precipitation[month]
        yearly_precipitation += precipitation_per_month
    print(f'Yearly Precipitation: {yearly_precipitation}')

    # 2.2 Relative monthly precipitation
    relative_monthly_precipitation = {}

    for month in location_monthly_precipitation:
        relative_value = location_monthly_precipitation[month] / yearly_precipitation
        relative_monthly_precipitation[month] = relative_value
    list_relative_monthly_precipitation = list(relative_monthly_precipitation.values())
    print(f'Relative monthly precipitation: {list_relative_monthly_precipitation}')

    # Saving results as JSON file
    stations_data[location] = {
        'station': station,
        'state': state,
        'total_monthly_precipitation': list_precipitation_monthly,
        'total_yearly_precipitation': yearly_precipitation,
        'relative_monthly_precipitation': list_relative_monthly_precipitation,
        'relative_yearly_precipitation': 0
    }


with open('results.json', 'w', encoding = 'utf-8') as file:       # Writing to a JSON file
        json.dump(stations_data, file, indent = 4)  