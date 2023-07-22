import requests
import json

response = requests.get('https://api.spacexdata.com/v4/launches/past')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print('Request failed with status code', response.status_code)
