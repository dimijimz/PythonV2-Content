import requests
from bs4 import BeautifulSoup
import pandas as pd

author = []
quotes = []
tags = []

for i in range(1, 11):
    response = requests.get(f"https://quotes.toscrape.com/page/{i}/")
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    for quote in soup.find_all("div", class_="quote"):
        author.append(quote.find("small", class_="author").text)
        quotes.append(quote.find("span", class_="text").text)

        for tag in quote.find_all("a", class_="tag"):
            tags.append(tag.text)


data = {"Author": author, "Quote": quotes, "Tags": tags}
df = pd.DataFrame(data)

print(df.head())