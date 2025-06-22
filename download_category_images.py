import os
import requests
from urllib.parse import quote
from django.utils.text import slugify  # Optional, or define your own

UNSPLASH_ACCESS_KEY = "0TIr1WywkFmeA6IX6AhpmjXtw50wbi7gVH7MZTq7En8"  # Replace this

categories = [
    "Electronics", "Fashion", "Home & Kitchen", "Beauty & Personal Care",
    "Sports & Outdoors", "Books", "Toys & Games", "Health & Wellness",
    "Grocery & Gourmet Foods", "Office Supplies", "Automotive", "Jewelry & Accessories",
    "Baby Products", "Footwear", "Mobile Phones & Accessories", "Furniture",
    "Pet Supplies", "Tools & Hardware", "Cameras & Photography", "Stationery & Craft"
]

SAVE_DIR = "static/category_images/"
os.makedirs(SAVE_DIR, exist_ok=True)

def custom_slugify(name):
    # Keep hyphens, remove ampersands and convert to lowercase
    return (
        name.lower()
        .replace(" & ", " ")
        .replace(" ", "-")
        .replace("&", "and")
    )

def download_image(query, filename):
    url = f"https://api.unsplash.com/photos/random?query={quote(query)}&client_id={UNSPLASH_ACCESS_KEY}&orientation=squarish"
    response = requests.get(url)
    
    if response.status_code == 200:
        image_url = response.json().get('urls', {}).get('regular')
        if image_url:
            image_data = requests.get(image_url).content
            with open(os.path.join(SAVE_DIR, filename), 'wb') as f:
                f.write(image_data)
            print(f"✔ Downloaded: {filename}")
        else:
            print(f"⚠ No image found for: {query}")
    else:
        print(f"❌ Error fetching image for {query} – Status code {response.status_code}")

for category in categories:
    slug = custom_slugify(category)
    filename = f"{slug}.jpg"
    download_image(category, filename)
