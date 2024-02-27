from flight_data import *

import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.twilio_from_number = os.environ["TWILIO_FROM_NUMBER"]
        self.twilio_to_number = os.environ["TWILIO_TO_NUMBER"]

    def send_notification(self, flight: FlightData):
        client = Client(self.twilio_account_sid, self.twilio_auth_token)

        body = f"CHEAP FLIGHT ALERT!\n{flight.to_str()}"
        client.messages.create(
            body=body,
            from_=self.twilio_from_number,
            to=self.twilio_to_number
        )
