from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import os
import smtplib
import requests


def send_email(content):
    text_subtype = 'plain'
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = "LOW PRICE ALERT!"
    msg['From'] = EMAIL_FROM

    print(f"Connecting to {SMTP_HOST}:{SMTP_PORT}")
    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as connection:
        print(f"Sending email to {EMAIL_TO}...")
        connection.sendmail(from_addr=EMAIL_FROM, to_addrs=[EMAIL_TO], msg=msg.as_string())
        print("Email sent!")
        connection.close()


SMTP_HOST = os.environ["SMTP_HOST"]
SMTP_PORT = os.environ["SMTP_PORT"]
EMAIL_FROM = os.environ["EMAIL_FROM"]
EMAIL_TO = os.environ["EMAIL_TO"]

AMAZON_URL = "https://www.amazon.com/Nintendo-eShop-Gift-Card-Digital/dp/B01LZZ8UKK/ref=sr_1_9?crid=2KRTXS8ADARJD&dib=eyJ2IjoiMSJ9.wBt6qPPJqeDmO5DUJ0II3OwC053oMUowHKrQ_0YsYNoUDi5p3caYCSUJTSiyq32ztPzjDd-26KijDNHNwNqDD6NBodY3_xAVB-08EeXgcdUzE2KE653K_5KApfx2H6o1rwoVhL03CSHe2IR_cJTf9w4mlE8EPK258R7Xt1H_FngXIWWOgOM3A8Q_hnJjMdUQEHbLbiRezRkVnR3WVMF1H6tuo917jHFuIGItw03T6D4.5qscx9IiSX_w1ESZP-0W9XjOFwu05lz_1HdpxpL4AsE&dib_tag=se&keywords=eshop&qid=1709560713&sprefix=eshop%2Caps%2C286&sr=8-9&th=1"
PRICE_THRESHOLD = 79.99
response = requests.get(AMAZON_URL, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "upgrade-insecure-requests": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "te": "trailers",
    "x-forwarded-proto": "https",
    "x-https": "on"
})
response.raise_for_status()
html = response.text

# Store HTML as a file to make development so we don't make too many requests to Amazon
# with open("website.html", "w") as html_file:
#     html_file.write(html)
#
# with open("website.html", "r") as html_file:
#     html = html_file.read()

soup = BeautifulSoup(html, "html.parser") # Use lxml?
price_raw = soup.select_one("#corePriceDisplay_desktop_feature_div .aok-offscreen").getText()
if price_raw is None:
    print("Price unavailable from webpage. Maybe the article is no longer available.")
else:
    price = round(float(price_raw.strip().replace("$", "")), 2)
    price_str = "{:.2f}".format(price)
    threshold_str = "{:.2f}".format(PRICE_THRESHOLD)
    if price <= PRICE_THRESHOLD:
        product_title = soup.select_one("#productTitle").getText().strip()
        send_email(f"{product_title}\n{AMAZON_URL}\nThreshold: ${threshold_str}\nNew low price: ${price_str}\nBUY NOW!")
