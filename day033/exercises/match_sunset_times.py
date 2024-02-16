import datetime
import requests

MY_LAT = -34.603683
MY_LONG = -58.381557
MY_TIMEZONE = "America/Argentina/Buenos_Aires"

params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": MY_TIMEZONE,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.datetime.now()

print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")
print(time_now.hour)
