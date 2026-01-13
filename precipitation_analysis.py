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
total_monthly_precipitation = {}
monthly_precipitation = 0
month = 0 

while month < 12:
    month += 1
    monthly_precipitation = 0
    for measurement in seattle_precipitation:
        year, month, day = measurement['date'].split('-') 
        if date_split[1] == month:
            monthly_precipitation += measurement['value']
    total_monthly_precipitation.append(monthly_precipitation)
print(total_monthly_precipitation)


# 1.4 Saving results as JSON file
results = {}
results['Seattle'] = {
    'station': 'GHCND:USW00093814',
    'state': 'OH',
    'total_monthly_precipitation': total_monthly_precipitation,
    'total_yearly_precipitation': 0,
    'relative_monthly_precipitation': [0] *12,
    'relative_yearly_precipitation': 0
}

with open('results.json', 'w', encoding = 'utf-8') as file:       # Writing to a JSON file
    json.dump(results, file, indent = 4)  