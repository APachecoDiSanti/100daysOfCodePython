from data_manager import *
from flight_search import *
from notification_manager import *

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

print("Getting destinations from Sheety...")
sheet_cities = data_manager.get_sheet_cities()

print("Updating Sheety with IATA codes...")
updated_sheet_cities = flight_search.get_iat_city_codes(sheet_cities)
data_manager.update_rows(updated_sheet_cities)

print("Getting destinations with IATA codes from Sheety...")
all_cities = data_manager.get_sheet_cities()

print("Searching for cheapest flights...")
cheapest_flights = flight_search.get_cheapest_flights_next_6_months(all_cities)
cheapest_cities = {city["iataCode"]: city["lowestPrice"] for city in all_cities["prices"]}

print("Get list of emails...")
club_users = data_manager.get_club_user_data()
club_emails = [user["email"] for user in club_users["users"]]
print(club_emails)

print("Sending notifications...")
for flight in cheapest_flights:
    if flight.price < cheapest_cities[flight.to_city]:
        print(flight.to_str())
        notification_manager.send_notification(flight)
        notification_manager.send_emails(club_emails, flight)
