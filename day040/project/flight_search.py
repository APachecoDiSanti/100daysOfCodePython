import os
import requests

from flight_data import *


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_base_url = "https://api.tequila.kiwi.com"
        self.tequila_api_key = os.environ["TEQUILA_API_KEY"]
        self.tequila_headers = {
                "apikey": self.tequila_api_key,
                "Content-Type": "application/json"
            }

    def get_city_info(self, city):
        response = requests.get(
            url=f"{self.tequila_base_url}/locations/query",
            headers=self.tequila_headers,
            params={
                "term": city,
                "location_types": "city",
                "limit": 1
            }
        )
        print(f"{response.status_code} => {response.json()}")
        response.raise_for_status()
        return response.json()

    def get_iat_city_codes(self, sheet_cities):
        for sheet_city in sheet_cities["prices"]:
            city_data = self.get_city_info(sheet_city["city"])
            sheet_city["iataCode"] = city_data["locations"][0]["code"]
        return sheet_cities

    def get_cheapest_flight(self, city, max_stopovers=0):
        tomorrow = datetime.datetime.today().date() + datetime.timedelta(days=1)
        tomorrow_plus_6_months = tomorrow + datetime.timedelta(days=180)
        iata_code = city["iataCode"]
        response = requests.get(
            url=f"{self.tequila_base_url}/search",
            headers=self.tequila_headers,
            params={
                "fly_from": "LON",
                "fly_to": iata_code,
                "date_from": tomorrow,
                "date_to": tomorrow_plus_6_months,
                "adults": 1,
                "one_for_city": 1,
                "curr": "GBP",
                "max_stopovers": max_stopovers
            }
        )
        print(f"{response.status_code} => {response.json()}")
        response.raise_for_status()
        try:
            flight = FlightData(response.json())
            return flight
        except IndexError:
            print(f"No direct flights found between LON and {iata_code}!")
            return None

    def get_cheapest_flights_next_6_months(self, sheet_cities):
        flights = []

        for sheet_city in sheet_cities["prices"]:
            flight = self.get_cheapest_flight(sheet_city)
            if flight is None:
                flight = self.get_cheapest_flight(sheet_city, 1)
            if flight is not None:
                flights.append(flight)

        return flights
