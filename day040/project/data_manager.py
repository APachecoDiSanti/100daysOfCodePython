import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_auth_token = os.environ["SHEETY_AUTH_TOKEN"]
        self.sheety_base_url = "https://api.sheety.co"
        self.sheety_user_id = os.environ["SHEETY_USER_ID"]

    def get_sheet_cities(self):
        response = requests.get(
            url=f"{self.sheety_base_url}/{self.sheety_user_id}/flightDeals/prices",
            headers={
                "Authorization": f"Bearer {self.sheety_auth_token}",
                "Content-Type": "application/json"
            }
        )
        print(f"{response.status_code} => {response.json()}")
        response.raise_for_status()
        return response.json()

    def update_rows(self, updated_rows):
        for updated_data in updated_rows["prices"]:
            print(updated_data)
            row_id = updated_data["id"]
            response = requests.put(
                url=f"{self.sheety_base_url}/{self.sheety_user_id}/flightDeals/prices/{row_id}",
                headers={
                    "Authorization": f"Bearer {self.sheety_auth_token}",
                    "Content-Type": "application/json"
                },
                json={
                    "price": updated_data
                }
            )
            print(f"{response.status_code} => {response.json()}")
            response.raise_for_status()

    def register_user(self, first_name, last_name, email):
        response = requests.post(
            url=f"{self.sheety_base_url}/{self.sheety_user_id}/flightDeals/users",
            headers={
                "Authorization": f"Bearer {self.sheety_auth_token}",
                "Content-Type": "application/json"
            },
            json={
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email
                }

            }
        )
        print(f"{response.status_code} => {response.json()}")
        response.raise_for_status()

    def get_club_user_data(self):
        response = requests.get(
            url=f"{self.sheety_base_url}/{self.sheety_user_id}/flightDeals/users",
            headers={
                "Authorization": f"Bearer {self.sheety_auth_token}",
                "Content-Type": "application/json"
            }
        )
        print(f"{response.status_code} => {response.json()}")
        response.raise_for_status()
        return response.json()
