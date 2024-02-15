import datetime as dt
import random
import os
import smtplib
from email.mime.text import MIMEText


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
    msg['Subject'] = "Motivational quote"
    msg['From'] = my_email

    print("Start")
    with smtplib.SMTP(host=smtp_host, port=smtp_port) as connection:
        print("TLS")
        connection.starttls()
        print("Login")
        connection.login(user=my_email, password=my_password)
        print("Sendmail")
        connection.sendmail(from_addr=my_email, to_addrs=[to_email], msg=msg.as_string())
        print("Close")
        connection.close()


# Thursday
EMAIL_DAY = 3

now = dt.datetime.now()
weekday = now.weekday()

if weekday == EMAIL_DAY:
    with open("quotes.txt") as quotes_files:
        quotes = quotes_files.readlines()
        quote = random.choice(quotes).strip()
        send_email(quote)
