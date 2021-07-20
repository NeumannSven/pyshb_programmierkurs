# OpenRouteService

## Distanzmessung

```python
import requests
import json

api_key="your_api_key"
country = "Germany"
profile = "foot-walking" #foot-walking | driving-car | cycling-regular
start_street = "Obernstrasse"
start_number = "15"
start_postalcode = "28195"
start_county = "Bremen"
start_city = "Bremen"

target_street = "Bornstrasse"
target_number = "13"
target_postalcode = "28195"
target_county = "Bremen"
target_city = "Bremen"

headers = {'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8'}

call = requests.get(f'https://api.openrouteservice.org/geocode/search/structured?api_key={api_key}&address={start_number}%20{start_street}&country={country}&postalcode={start_postalcode}&county={start_county}&locality={start_city}', headers=headers)
start = json.loads(call.text)
start = start['bbox'][:2]

call = requests.get(f'https://api.openrouteservice.org/geocode/search/structured?api_key={api_key}&address={target_number}%20{target_street}&country={country}&postalcode={target_postalcode}&county={target_county}&locality={target_city}', headers=headers)
target = json.loads(call.text)
target = target['bbox'][:2]

call = requests.get(f'https://api.openrouteservice.org/v2/directions/{profile}?api_key={api_key}&start={start[0]},%20{start[1]}&end={target[0]},%20{target[1]}', headers=headers)
distance = json.loads(call.text)
print(distance['features'][0]['properties']['segments'][0]['distance'])
```
