import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

body = response.json()
longitude = body["iss_position"]["longitude"]
latitude = body["iss_position"]["latitude"]
iss_position = (longitude, latitude)
#print(iss_position) #('158.2589', '-48.4525')

