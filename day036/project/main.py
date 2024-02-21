import datetime
import os
import requests
from twilio.rest import Client


def get_data_from_previous_business_day(day, stock_data):
    previous_business_day = day - datetime.timedelta(days=1)
    previous_business_day_data = stock_data.get(str(previous_business_day))
    while previous_business_day_data is None:
        previous_business_day = previous_business_day - datetime.timedelta(days=1)
        previous_business_day_data = stock_data.get(str(previous_business_day))
    return previous_business_day, previous_business_day_data


def get_stock_data():
    response = requests.get(url=AV_BASE_URL, params={
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": AV_API_KEY
    })
    response.raise_for_status()

    return response.json()


def get_company_news(date):
    response = requests.get(url=NA_BASE_URL, params={
        "q": COMPANY_NAME,
        "from": date,
        "sortBy": "popularity",
        "pageSize": 3,
        "page": 1,
        "apiKey": NA_API_KEY
    })
    response.raise_for_status()

    return response.json()


def send_sms(stock_news, percentage_diff):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for new in stock_news:
        body = f"""{STOCK}: {percentage_diff}
Headline: {new["headline"]}
Brief: {new["brief"]}
"""
        client.messages.create(
            body=body,
            from_=TWILIO_NUMBER,
            to=TO_NUMBER
        )


AV_API_KEY = os.environ["AV_API_KEY"]
AV_BASE_URL = "https://www.alphavantage.co/query"

NA_API_KEY = os.environ["NA_API_KEY"]
NA_BASE_URL = "https://newsapi.org/v2/everything"

TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TO_NUMBER = os.environ["TO_NUMBER"]

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

DIFFERENCE_THRESHOLD_PERCENTAGE = 5

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
data = get_stock_data()

time_series_daily = data["Time Series (Daily)"]
today = datetime.datetime.today().date()

previous_day, previous_day_data = get_data_from_previous_business_day(today, time_series_daily)
_, day_before_previous_day_data = get_data_from_previous_business_day(previous_day, time_series_daily)

close_previous_day = float(previous_day_data["4. close"])
close_day_before_previous_day = float(day_before_previous_day_data["4. close"])

difference_in_price = abs(close_previous_day - close_day_before_previous_day)
percentage_difference = (difference_in_price / close_previous_day) * 100
difference_symbol = "🔻" if close_previous_day < close_day_before_previous_day else "🔺"
percentage_difference_with_symbol = difference_symbol+str(round(percentage_difference, 2))+"%"

print(percentage_difference_with_symbol)
if percentage_difference <= DIFFERENCE_THRESHOLD_PERCENTAGE:
    print(f"Stock variance is lower than {DIFFERENCE_THRESHOLD_PERCENTAGE}%. No news will be sent.")
else:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news = get_company_news(str(previous_day))
    relevant_news = [{"headline": article["title"], "brief": article["description"]} for article in news["articles"]]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    send_sms(relevant_news, percentage_difference_with_symbol)
    print("Sent news via SMS!")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

