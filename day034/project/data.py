import requests


def get_question_data():
    response = requests.get(url="https://opentdb.com/api.php", params={
        "amount": 10,
        "type": "boolean"
    })
    response.raise_for_status()
    return response.json()["results"]


question_data = get_question_data()
