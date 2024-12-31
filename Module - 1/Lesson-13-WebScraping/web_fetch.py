import requests
from bs4 import BeautifulSoup

response = requests.get("http://journeytolunar.com")
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

h1_tag = soup.find("h1")

paragraphs = soup.find_all("p")

for paragraph in paragraphs:
    print(paragraph)

content = soup.find("div", class_="intro")

print(content)