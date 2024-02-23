import datetime
import requests
import os


def get_exercise_stats(natural_description, weight_kg, height_cm, age):
    response = requests.post(
        url=f"{NIX_BASE_URL}/v2/natural/exercise",
        headers={
            "x-app-id": NIX_APP_ID,
            "x-app-key": NIX_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "query": natural_description,
            "weight_kg": weight_kg,
            "height_cm": height_cm,
            "age": age
        }
    )
    print(f"{response.status_code} => {response.json()}")
    response.raise_for_status()
    return response.json()


def add_data_row(exercises_data):
    response = requests.post(
        url=f"{SHEETY_BASE_URL}/{SHEETY_USER_ID}/myWorkouts/workouts",
        headers={
            "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}",
            "Content-Type": "application/json"
        },
        json=exercises_data
    )
    print(f"{response.status_code} => {response.json()}")
    response.raise_for_status()
    return response.json()

NIX_BASE_URL = "https://trackapi.nutritionix.com"
NIX_APP_ID = os.environ["NIX_APP_ID"]
NIX_API_KEY = os.environ["NIX_API_KEY"]

MY_WEIGHT_KG = os.environ["MY_WEIGHT_KG"]
MY_HEIGHT_CM = os.environ["MY_HEIGHT_CM"]
MY_AGE = os.environ["MY_AGE"]

SHEETY_BASE_URL = "https://api.sheety.co"
SHEETY_USER_ID = os.environ["SHEETY_USER_ID"]
SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]


user_input = input("What exercise do you want to log?")
processed_data = get_exercise_stats(user_input, MY_WEIGHT_KG, MY_HEIGHT_CM, MY_AGE)

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for exercise in processed_data["exercises"]:
    add_data_row({
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    })

