from form_filler import *
from bs4 import BeautifulSoup
import requests

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"


def get_list_of_properties():
    response = requests.get(ZILLOW_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    estates = soup.select("ul article")

    data = []
    for estate in estates:
        link = estate.find(name="a").attrs["href"]
        address = estate.find(name="address").text.split("|")[-1].strip()
        price_str = estate.find(attrs={"data-test": "property-card-price"}).text.strip().split("/")[0].split(" ")[0]
        price = price_str.replace("+", "")
        data.append({
            "address": address,
            "price": price,
            "link": link
        })
    return data


data_dict = get_list_of_properties()
form_filler = FormFiller(data_dict)
form_filler.input_data()
