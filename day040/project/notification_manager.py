from flight_data import *

from email.mime.text import MIMEText
import os
import smtplib
from twilio.rest import Client



class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.twilio_from_number = os.environ["TWILIO_FROM_NUMBER"]
        self.twilio_to_number = os.environ["TWILIO_TO_NUMBER"]
        self.mailosaur_email = os.environ["MAILOSAUR_EMAIL"]
        self.mailosaur_password = os.environ["MAILOSAUR_PASSWORD"]
        self.mailosaur_smtp_host = os.environ["MAILOSAUR_SMTP_HOST"]
        self.mailosaur_smtp_port = int(os.environ["MAILOSAUR_SMTP_PORT"])

    def send_notification(self, flight: FlightData):
        client = Client(self.twilio_account_sid, self.twilio_auth_token)

        body = f"CHEAP FLIGHT ALERT!\n{flight.to_str()}"
        client.messages.create(
            body=body,
            from_=self.twilio_from_number,
            to=self.twilio_to_number
        )

    def send_emails(self, emails, flight: FlightData):
        msg = MIMEText(flight.to_str(), "plain")
        msg["Subject"] = "Agustin's Flight Club - Cheap flight alert!"
        msg["From"] = self.mailosaur_email

        for email in emails:
            print(f"Connecting to {self.mailosaur_smtp_host}:{self.mailosaur_smtp_port}")
            with smtplib.SMTP(host=self.mailosaur_smtp_host, port=self.mailosaur_smtp_port) as connection:
                print("Using TLS...")
                connection.starttls()
                print(f"Login in as {self.mailosaur_email}...")
                connection.login(user=self.mailosaur_email, password=self.mailosaur_password)
                print(f"Sending email to {email}...")
                connection.sendmail(from_addr=self.mailosaur_email, to_addrs=[email], msg=msg.as_string())
                print("Email sent!")
                connection.close()
