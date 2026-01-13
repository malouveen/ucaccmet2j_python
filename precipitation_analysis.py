#Import necesarry packages
import json

# Opening and reading the files
with open('precipitation.json') as file:                                                    # Opening the precipitation data file 
    precipitation_data = json.load(file) 
  
with open('stations.csv') as file:                                                          # Opening the stations csv file
    first_line = file.readline()                                                            # Reading the first line manually
    stations = file.readlines()                                                             # Reading the other lines

# Creating a dictionary from stations csv data
stations_data = {}                                                                          # Creating an empty dicitonary for station data
for lines in stations:
    location, state, station = lines.split(',')                                             # Splitting the lines by comma's 
    stations_data[location] = {'station': station.strip(), 'state':state}                   # Appending in format necessary for plotting

# Looping over each location
for location in stations_data:
    location_dictionary = stations_data[location]
    station = location_dictionary['station']                                                # Storing station codes in variable 'station'
    state = location_dictionary['state']                                                    # Storing states in variable 'state'

    # 1.2 Selecting the measurements belonging to specific location data
    location_precipitation = []                                                             # Creating an empty list for precipitation at location
    total_precipitation_all_cities = 0                                                      # Stetting total precipitation to 0 

    for measurement in precipitation_data:
        if measurement['station'] == station:
            location_precipitation.append(measurement)                                      # Appending each measurement to its respective location
        total_precipitation_all_cities += measurement['value']                              # Calculating total precpitaton across all cities   
    
    # 1.3 Total monthly precipitation
    location_monthly_precipitation = {}                                                     # Creating an empty dictionary for monthly precipitation at location
    
    for measurement in location_precipitation:
        year, month, day = measurement['date'].split('-')                                   # Splitting the date by '-'
        if month not in location_monthly_precipitation:                             
            monthly_precipitation = 0
        monthly_precipitation += measurement['value']                                       # Adding measurement values to respective month at location
        location_monthly_precipitation[month] = monthly_precipitation
    list_precipitation_monthly = list(location_monthly_precipitation.values())              # Creating a list from the dictionary

    # 2.1 Total yearly precipitation per location 
    yearly_precipitation = 0

    for month in location_monthly_precipitation:
        yearly_precipitation += location_monthly_precipitation[month]                       # Adding monthly precipitation to yearly total value

    # 2.2 Relative monthly precipitation
    relative_monthly_precipitation = {}                                                     # Create an empty dictionary for relative monthly precipitation

    for month in location_monthly_precipitation:
        relative_monthly_precipitation[month] = location_monthly_precipitation[month] / yearly_precipitation        # Deviding monthly precipitation by yearly value 
    list_relative_monthly_precipitation = list(relative_monthly_precipitation.values())                             # Creating a list from dictionary 

    # 3.2 Relative yearly precipitation
    relative_yearly_precipitation = yearly_precipitation / total_precipitation_all_cities   # Yearly precipitation at locating / total precipitation over all cities

    # Saving results as JSON file
    stations_data[location] = {
        'station': station,
        'state': state,
        'total_monthly_precipitation': list_precipitation_monthly,
        'total_yearly_precipitation': yearly_precipitation,
        'relative_monthly_precipitation': list_relative_monthly_precipitation,
        'relative_yearly_precipitation': relative_yearly_precipitation
    }

with open('results.json', 'w', encoding = 'utf-8') as file:                                 # Writing to a JSON file
        json.dump(stations_data, file, indent = 4)  
