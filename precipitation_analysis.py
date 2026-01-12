#Import necesarry packages
import json

# Opening and reading the file
with open('precipitation.json') as file:  
    precipitation_data = json.load(file)                               

# 1.2 Selecting the measurements belonging to Seattle data
seattle_precipitation = []
for seattle in precipitation_data:
    if seattle['station'] == 'GHCND:US1WAKG0038':
        seattle_precipitation.append(seattle)
print(seattle_precipitation)

# 1.3 Calculating total monthly precipitation
total_monthly_precipitation = []
monthly_precipitation = 0
month = 0 

while month < 13:
    month += 1
    for measurement in seattle_precipitation:
        if measurement['date'].startswith(f'2010-0{month}'):
            monthly_precipitation += measurement['value']
    total_monthly_precipitation.append(monthly_precipitation)
print(total_monthly_precipitation)
