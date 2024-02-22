import datetime
import os
import requests


def create_account():
    response = requests.post(url=f"{PIXELA_BASE_URL}/v1/users", json={
        "token": PIXELA_AUTH_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    })
    print(response.status_code)
    print(response.json())
    response.raise_for_status()


def create_graph(graph_id, graph_name, graph_unit, graph_type, graph_color):
    response = requests.post(
        url=f"{PIXELA_BASE_URL}/v1/users/{PIXELA_USERNAME}/graphs",
        json={
            "id": graph_id,
            "name": graph_name,
            "unit": graph_unit,
            "type": graph_type,
            "color": graph_color
        },
        headers={
            "X-USER-TOKEN": PIXELA_AUTH_TOKEN
        }
    )
    print(response.status_code)
    print(response.json())
    response.raise_for_status()


def post_pixel(graph_id, date, quantity):
    response = requests.post(
        url=f"{PIXELA_BASE_URL}/v1/users/{PIXELA_USERNAME}/graphs/{graph_id}",
        json={
            "date": date,
            "quantity": quantity
        },
        headers={
            "X-USER-TOKEN": PIXELA_AUTH_TOKEN
        }
    )
    print(response.status_code)
    print(response.json())
    response.raise_for_status()


def update_pixel(graph_id, date, quantity):
    response = requests.put(
        url=f"{PIXELA_BASE_URL}/v1/users/{PIXELA_USERNAME}/graphs/{graph_id}/{date}",
        json={
            "quantity": quantity
        },
        headers={
            "X-USER-TOKEN": PIXELA_AUTH_TOKEN
        }
    )
    print(response.status_code)
    print(response.json())
    response.raise_for_status()


def delete_pixel(graph_id, date):
    response = requests.delete(
        url=f"{PIXELA_BASE_URL}/v1/users/{PIXELA_USERNAME}/graphs/{graph_id}/{date}",
        headers={
            "X-USER-TOKEN": PIXELA_AUTH_TOKEN
        }
    )
    print(response.status_code)
    print(response.json())
    response.raise_for_status()


PIXELA_BASE_URL = "https://pixe.la"
PIXELA_AUTH_TOKEN = os.environ["PIXELA_AUTH_TOKEN"]
PIXELA_USERNAME = os.environ["PIXELA_USERNAME"]
PIXELA_GRAPH_ID = "exercise"


create_account()
create_graph(PIXELA_GRAPH_ID, "Exercise Activity", "minutes", "int", "momiji")

today = datetime.date.today().strftime("%Y%m%d")
post_pixel(PIXELA_GRAPH_ID, today, "5")
update_pixel(PIXELA_GRAPH_ID, today, "15")
delete_pixel(PIXELA_GRAPH_ID, today)
