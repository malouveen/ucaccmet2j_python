#Import necesarry packages
import json

# Opening and reading the file
with open('precipitation.json') as file:  
    precipitation_data = json.load(file)                               

# Selecting the measurements belonging to Seattle data
seattle_precipitation = []
for seattle in precipitation_data:
    if seattle["station"] == 'GHCND:US1WAKG0038':
        seattle_precipitation.append(seattle)
print(seattle_precipitation)

