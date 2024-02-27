import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, tequila_flight_data):
        self.from_city = tequila_flight_data["data"][0]["cityCodeFrom"]
        self.to_city = tequila_flight_data["data"][0]["cityCodeTo"]
        self.currency = tequila_flight_data["currency"]
        self.price = tequila_flight_data["data"][0]["price"]
        self.date = datetime.datetime.fromtimestamp(tequila_flight_data["data"][0]["dTimeUTC"]).strftime("%Y/%m/%d %H:%M:%S")
        self.duration = tequila_flight_data["data"][0]["fly_duration"]

    def to_str(self):
        return f"""FROM: {self.from_city}
TO: {self.to_city}
PRICE: {self.currency} {self.price}
DATE: {self.date}
DURATION: {self.duration}
"""
