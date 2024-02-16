from config import *
import datetime
from email.mime.text import MIMEText
import os
import requests
import smtplib
import time



def send_email(content):
    # Never save credentials in GitHub
    # they can get scraped if on a public repository, or they can be leaked on a private repository
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT"))
    to_email = os.getenv("TO_EMAIL")

    text_subtype = 'plain'
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = "ISS has been detected in the sky"
    msg['From'] = my_email

    print(f"Connecting to {smtp_host}:{smtp_port}")
    with smtplib.SMTP(host=smtp_host, port=smtp_port) as connection:
        print("Using TLS...")
        connection.starttls()
        print(f"Login in as {my_email}...")
        connection.login(user=my_email, password=my_password)
        print(f"Sending email to {to_email}...")
        connection.sendmail(from_addr=my_email, to_addrs=[to_email], msg=msg.as_string())
        print("Email sent!")
        connection.close()


def is_it_currently_dark():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "tzid": MY_TIMEZONE,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_time = sunrise.split("T")[1].split("-")[0].split(":")
    sunset_time = sunset.split("T")[1].split("-")[0].split(":")
    time_now = str(datetime.datetime.now()).split(" ")[1].split(".")[0].split(":")

    # https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
    # The comparison uses lexicographical ordering: first the first two items are compared,
    # and if they differ this determines the outcome of the comparison; if they are equal,
    # the next two items are compared, and so on, until either sequence is exhausted.
    #
    # In our use case it means that the times will be compared and if they are equal hours it will check the minutes and
    # if the minutes are equal then the seconds will be checked.
    return time_now <= sunrise_time or time_now >= sunset_time


def is_the_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    return abs(MY_LAT - latitude) < ERROR_MARGIN and abs(MY_LONG - longitude) < ERROR_MARGIN


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# Your position is within +5 or -5 degrees of the ISS position.

while True:
    time.sleep(300)
    now = datetime.datetime.now()
    print(f"{now} - Checking...")
    if is_the_iss_close() and is_it_currently_dark():
        send_email("The ISS is currently visible in the sky!\nGo outside!\n\nSincerely,\nBOTISS")