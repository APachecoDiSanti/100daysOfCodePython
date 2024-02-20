import os
import requests
from twilio.rest import Client

TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TO_NUMBER = os.environ["TO_NUMBER"]

OW_API_KEY = os.environ["OW_API_KEY"]
MY_LAT = -34.603683
MY_LON = -58.381557
OW_URL = "https://api.openweathermap.org/data/2.5/forecast"
NUMBER_OF_FORECASTS = 4


def get_weather_forecast_for_next_12_hours():
    response = requests.get(url=OW_URL, params={
        "lat": MY_LAT,
        "lon": MY_LON,
        "appid": OW_API_KEY,
        "cnt": NUMBER_OF_FORECASTS
    })
    response.raise_for_status()

    # print(response.status_code)
    # The first 4 forecasts in the list cover the next 12 hours
    # The cnt=4 parameter will let us only request these 4 3 hour forecasts
    return response.json()


data = get_weather_forecast_for_next_12_hours()
data_list = data["list"]
print(data_list)

for window in data_list:
    relevant_forecasts = [weather["id"] for weather in window["weather"] if weather["id"] < 700]
    if len(relevant_forecasts) > 0:
        print(relevant_forecasts)
        print("Bring an umbrella!")
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
            body="It's going to rain today. Bring an umbrella!",
            from_=TWILIO_NUMBER,
            to=TO_NUMBER
        )

        print(message.status)
        break
