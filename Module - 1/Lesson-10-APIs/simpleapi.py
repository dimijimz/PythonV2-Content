import requests

API_KEY = "live_YPQewc9YPMUyHHI76NSZHA69VlVOKe5yrF7Rr4XZh8VJdsVyKQ3m7ZDyWPXMxWbQ"
BASE_URL = "https://api.thecatapi.com/v1"

# Headers for authentication
HEADERS = {"x-api-key": API_KEY}

def get_random_cat_image():
    """Fetch a random cat image."""
    try:
        response = requests.get(f"{BASE_URL}/images/search", headers=HEADERS)
        response.raise_for_status()
        cat_image = response.json()[0]
        print(f"Here is a random cat image URL: {cat_image['url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cat image: {e}")

def post_favorite_cat(cat_id):
    """Post a favorite cat image."""
    try:
        data = {"image_id": cat_id}
        response = requests.post(f"{BASE_URL}/favourites", headers=HEADERS, json=data)
        response.raise_for_status()
        favorite = response.json()
        print(f"Successfully added cat to favorites! Favorite ID: {favorite['id']}")
    except requests.exceptions.RequestException as e:
        print(f"Error favoriting cat: {e}")

def main():
    print("Welcome to the Cat API Client!")
    while True:
        print("\nOptions:")
        print("1. Get a random cat image")
        print("2. Favorite a cat image (requires cat image ID)")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            get_random_cat_image()
        elif choice == "2":
            cat_id = input("Enter the cat image ID to favorite: ").strip()
            post_favorite_cat(cat_id)
        elif choice == "3":
            print("Goodbye! 🐾")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
