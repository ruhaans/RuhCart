import os
import requests
from urllib.parse import quote
from django.utils.text import slugify  # If not using Django, use a custom slugify below

UNSPLASH_ACCESS_KEY = "iBFojcGj_fH-QacybUlclx6oE_jW5Dr3lAETElX8ypU"  # ← Replace this

SAVE_DIR = "static/product_images/"
os.makedirs(SAVE_DIR, exist_ok=True)

products = [
    "Bluetooth Speaker", "Wireless Earbuds", "Smart Watch", "USB-C Cable",
    "Men's T-Shirt", "Women's Jeans", "Sunglasses", "Leather Belt",
    "Air Fryer", "Spice Rack", "Nonstick Pan", "Cushion Covers",
    "Face Serum", "Lipstick", "Body Lotion", "Hair Oil",
    "Yoga Mat", "Dumbbells", "Skipping Rope", "Trekking Bag",
    "Fiction Novel", "Self-Help Book", "Science Encyclopedia", "Notebook Set",
    "Lego Set", "Rubik's Cube", "Puzzle Board", "Remote Car",
    "Multivitamin", "Yoga Strap", "Protein Powder", "Essential Oils",
    "Almonds Pack", "Olive Oil", "Herbal Tea", "Chocolate Spread",
    "Ball Pens", "Sticky Notes", "File Folders", "Stapler Set",
    "Car Air Freshener", "Car Charger", "Seat Cover", "Tyre Pressure Gauge",
    "Stud Earrings", "Charm Bracelet", "Gold Ring", "Wrist Watch",
    "Baby Wipes", "Baby Lotion", "Pacifier Set", "Teething Ring",
    "Running Shoes", "Sandals", "Boots", "Loafers",
    "Phone Case", "Pop Socket", "Screen Guard", "Car Mount",
    "Study Table", "Shoe Rack", "Bean Bag", "Wooden Chair",
    "Dog Food", "Cat Toy", "Pet Shampoo", "Feeding Bowl",
    "Hammer Set", "Screwdriver Kit", "Measuring Tape", "Wrench Set",
    "Tripod Stand", "Camera Strap", "Memory Card", "Lens Cleaner",
    "Sketch Pens", "Watercolors", "Drawing Book", "Craft Paper"
]

# If not using Django:
# def slugify(name): return name.lower().replace('&', 'and').replace(' ', '-')

def download_image(product_name):
    slug = slugify(product_name)
    filename = f"{slug}.jpg"
    filepath = os.path.join(SAVE_DIR, filename)

    if os.path.exists(filepath):
        print(f"✔ Already exists: {filename}")
        return

    print(f"🔍 Searching: {product_name}")
    query = quote(product_name)
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}&orientation=squarish"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        image_url = data.get("urls", {}).get("regular")

        if not image_url:
            print(f"⚠ No image found for: {product_name}")
            return

        image_data = requests.get(image_url).content
        with open(filepath, "wb") as f:
            f.write(image_data)
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Failed for {product_name}: {e}")

# Download images
for product in products:
    download_image(product)
