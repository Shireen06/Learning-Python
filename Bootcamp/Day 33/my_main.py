# -*- coding: utf-8 -*-

import requests
from datetime import datetime

my_lat = -33.756088
my_long = 151.150070
 
 
parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0,}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now)
