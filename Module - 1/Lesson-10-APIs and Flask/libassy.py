import requests

url = "https://jsonplaceholder.typicode.com/posts" 

response = requests.get(url, timeout=5)

if response.status_code == 200:
    data = response.json()
    #print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

#Task 2

payload = {"name": "Bob", "email": "john.doe@example", "phone": "123-456-7890", "user_id": 1}

response = requests.post(url, json=payload, timeout=5)

if response.status_code == 201:
    created_post = response.json()
    print("User created successfully!")
else:
    print(f"Failed to create post. Status code: {response.status_code}")

#Task 2b
post_id = created_post["user_id"]
updated_payload = {"email": "cJFVW@example.com"}
response = requests.put(f"{url}/{post_id}", json=updated_payload, timeout=5)

if response.status_code == 200:
    updated_post = response.json()
    print("Post updated successfully!")
    print(updated_post)
else:
    print(f"Failed to update post. Status code: {response.status_code}")
#Task 3
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')
except Exception as err:
    print(f'Other error occurred: {err}')

#Task 4
#added timeout=5 to response lines
