from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")

response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article in articles:
    anchor = article.find("a")
    text = anchor.getText()
    article_texts.append(text)
    link = anchor.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])
