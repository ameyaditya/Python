from pprint import pprint
import requests

r = requests.get('api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=0539b61eba031b790590082e383f4e9a')
pprint(r.json())
