from bs4 import BeautifulSoup
import requests

website_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=website_url)
response.raise_for_status()

bs = BeautifulSoup(response.text, "html.parser")
all_titles = bs.find_all(name="h3", class_="title")

with open("movies.txt", "w") as movie_file:
    for i in range(len(all_titles)-1, -1, -1):
        h3 = all_titles[i]
        movie_file.write(h3.getText()+"\n")
