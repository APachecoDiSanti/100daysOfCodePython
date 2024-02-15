##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import os
import smtplib
from email.mime.text import MIMEText


def send_email(content, to_email):
    # Never save credentials in GitHub
    # they can get scraped if on a public repository, or they can be leaked on a private repository
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT"))

    text_subtype = 'plain'
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = "Happy Birthday!!!"
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


def prepare_message(name):
    number = random.randint(1, 3)
    with open(f"letter_templates/letter_{number}.txt") as template_file:
        template = template_file.read()
        return template.replace("[NAME]", name)


# START
now = dt.datetime.now()
month = now.month
day = now.day
birthdays = pandas.read_csv("birthdays.csv")
today_birthdays = birthdays.query(f"month == {month} & day == {day}")

for (index, row) in today_birthdays.iterrows():
    message = prepare_message(row["name"])
    send_email(message, row["email"])
