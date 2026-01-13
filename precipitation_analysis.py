#Import necesarry packages
import json

# Opening and reading the files
with open('precipitation.json') as file:  
    precipitation_data = json.load(file)     

# with open('station.csv')'
          
#           for mine in fole 
#           split by comma 

# Creating a dictionary with {Station:Code}


station_dictionary = {
    'Cincinnati': {
        'station': 'GHCND:USW00093814',
        'state': 'OH'
    },
    'Seattle': {
        'station': 'GHCND:US1WAKG0038',
        'state': 'WA'
    },
    'Maui': {
        'station': 'GHCND:USC00513317',
        'state': 'HI'
    },
    'San Diego': {
        'station': 'GHCND:US1CASD0032',
        'state': 'CA'
    }
}

for location in station_dictionary:
    location_dictionary = station_dictionary[location]
    station = location_dictionary['station']
    state = location_dictionary['state']
    print(state)

if location not in station_dictionary:
    station_dictionary = 0
    station_dictionary[location] = location


# # 1.2 Selecting the measurements belonging to Seattle data
seattle_precipitation = []
for seattle in precipitation_data:
    if seattle['station'] == 'GHCND:US1WAKG0038':
        seattle_precipitation.append(seattle)

# 1.3 Total monthly precipitation
total_monthly_precipitation = {}
 
for measurement in seattle_precipitation:
    year, month, day = measurement['date'].split('-') 
    if month not in total_monthly_precipitation:
        monthly_precipitation = 0
    monthly_precipitation += measurement['value']
    total_monthly_precipitation[month] = monthly_precipitation
list_precipitation_monthly = list(total_monthly_precipitation.values())
print(f'Monthy Precipitation: {list_precipitation_monthly}')

# 2.1 Total yearly precipitation
yearly_precipitation = 0

for month in total_monthly_precipitation:
    precipitation_per_month = total_monthly_precipitation[month]
    yearly_precipitation += precipitation_per_month
print(f'Yearly Precipitation: {yearly_precipitation}')

# 2.2 Relative monthly precipitation
relative_monthly_precipitation = {}

for month in total_monthly_precipitation:
    relative_value = total_monthly_precipitation[month] / yearly_precipitation
    relative_monthly_precipitation[month] = relative_value
list_relative_monthly_precipitation = list(relative_monthly_precipitation.values())
print(f'Relative monthly precipitation: {list_relative_monthly_precipitation}')

# Saving results as JSON file
results = {}
results['Seattle'] = {
    'station': 'GHCND:USW00093814',
    'state': 'OH',
    'total_monthly_precipitation': list_precipitation_monthly,
    'total_yearly_precipitation': yearly_precipitation,
    'relative_monthly_precipitation': list_relative_monthly_precipitation,
    'relative_yearly_precipitation': 0
}

with open('results.json', 'w', encoding = 'utf-8') as file:       # Writing to a JSON file
    json.dump(results, file, indent = 4)  