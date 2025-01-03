import requests
api_key = "74ceced274917000bd931fabb5c7f391"

city = "New York"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data) 