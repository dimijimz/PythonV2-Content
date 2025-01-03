from bs4 import BeautifulSoup
import requests
import pandas as pd
import nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Fetch the webpage
response = requests.get('http://books.toscrape.com')
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize lists to store scraped data
titles = []
prices = []
availability = []

# Loop through each book
for book in soup.find_all('article', class_='product_pod'):
    # Extract title
    titles.append(book.find('h3').find('a')['title'])
    
    # Extract price (removing the pound sign)
    prices.append(float(book.find('p', class_='price_color').text[2:]))
    
    # Extract availability
    availability.append(book.find('p', class_='instock availability').text.strip())

# Create a DataFrame
data = {'Title': titles, 'Price (£)': prices, 'Availability': availability}
df = pd.DataFrame(data)

# Analyze the data
# Count how many books are under £10
books_under_20 = df[df['Price (£)'] < 20].shape[0]

# Output results
average_price = df['Price (£)'].mean()
print(f"Average Price: £{average_price:.2f}")
print(f"Number of books under £20: {books_under_20}")
print(df.head())  # Display the first few rows of the DataFrame