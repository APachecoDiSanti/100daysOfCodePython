from bs4 import BeautifulSoup
# import lxml

with open("website.html") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)
