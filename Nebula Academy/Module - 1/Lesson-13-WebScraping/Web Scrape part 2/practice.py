from bs4 import BeautifulSoup
import requests
import pandas as pd

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get('https://www.goodreads.com/list/show/1652.Favorite_picture_books', headers=headers)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

tr_tags = soup.find_all('tr')
author = []
title = []
stars = []
for idx, tr in enumerate(tr_tags, start=1):

    book_title = tr.find('a', class_='bookTitle').text.strip()
    star_span = tr.find('span', class_='minirating').text[1:5]
    author_name = tr.find('a', class_='authorName').text
    if not is_number(star_span):
        continue
    author.append(author_name)
    title.append(book_title)
    stars.append(star_span)
    book_info = [book_title,star_span,author_name]


df = pd.DataFrame({"Author":author, "Title":title, "stars":stars})
print(df.head())

df['Rating'] = pd.to_numeric(df['stars'])
print(df.head())

top_10_rating = df.nlargest(10,'Rating')
print(top_10_rating['Rating'].mean())
print(top_10_rating)
top_author = top_10_rating.groupby('Author').count()
print(top_author)

print(len(tr_tags))
 