import requests
import json
import pandas as pd

response = requests.get('https://api.spacexdata.com/v4/launches/past')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv('spacex_launches.csv', index=False)
    print('Data fetched and saved')
else:
    print('Request failed with status code', response.status_code)
