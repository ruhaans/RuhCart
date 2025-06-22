import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruhcart.settings')  # Replace 'RuhCart' with your project name if different
django.setup()

import random
from django.core.files import File
from django.utils.text import slugify
from accounts.models import  User
from store.models import Product, Category  # Update 'yourapp' accordingly

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Adjust if running outside manage.py shell
IMAGE_SOURCE_DIR = os.path.join(BASE_DIR, 'static/product_images')

sellers = {
    "rohit": User.objects.get(username="rohit"),
    "neha": User.objects.get(username="neha"),
    "aman": User.objects.get(username="aman")
}

sample_products = {
    "Electronics": ["Bluetooth Speaker", "Wireless Earbuds", "Smart Watch", "USB-C Cable"],
    "Fashion": ["Men's T-Shirt", "Women's Jeans", "Sunglasses", "Leather Belt"],
    "Home & Kitchen": ["Air Fryer", "Spice Rack", "Nonstick Pan", "Cushion Covers"],
    "Beauty & Personal Care": ["Face Serum", "Lipstick", "Body Lotion", "Hair Oil"],
    "Sports & Outdoors": ["Yoga Mat", "Dumbbells", "Skipping Rope", "Trekking Bag"],
    "Books": ["Fiction Novel", "Self-Help Book", "Science Encyclopedia", "Notebook Set"],
    "Toys & Games": ["Lego Set", "Rubik's Cube", "Puzzle Board", "Remote Car"],
    "Health & Wellness": ["Multivitamin", "Yoga Strap", "Protein Powder", "Essential Oils"],
    "Grocery & Gourmet Foods": ["Almonds Pack", "Olive Oil", "Herbal Tea", "Chocolate Spread"],
    "Office Supplies": ["Ball Pens", "Sticky Notes", "File Folders", "Stapler Set"],
    "Automotive": ["Car Air Freshener", "Car Charger", "Seat Cover", "Tyre Pressure Gauge"],
    "Jewelry & Accessories": ["Stud Earrings", "Charm Bracelet", "Gold Ring", "Wrist Watch"],
    "Baby Products": ["Baby Wipes", "Baby Lotion", "Pacifier Set", "Teething Ring"],
    "Footwear": ["Running Shoes", "Sandals", "Boots", "Loafers"],
    "Mobile Phones & Accessories": ["Phone Case", "Pop Socket", "Screen Guard", "Car Mount"],
    "Furniture": ["Study Table", "Shoe Rack", "Bean Bag", "Wooden Chair"],
    "Pet Supplies": ["Dog Food", "Cat Toy", "Pet Shampoo", "Feeding Bowl"],
    "Tools & Hardware": ["Hammer Set", "Screwdriver Kit", "Measuring Tape", "Wrench Set"],
    "Cameras & Photography": ["Tripod Stand", "Camera Strap", "Memory Card", "Lens Cleaner"],
    "Stationery & Craft": ["Sketch Pens", "Watercolors", "Drawing Book", "Craft Paper"]
}

for cat_name, items in sample_products.items():
    try:
        category = Category.objects.get(name=cat_name)
    except Category.DoesNotExist:
        print(f"❌ Category not found: {cat_name}")
        continue

    for name in items:
        slug = slugify(name)
        image_path = os.path.join(IMAGE_SOURCE_DIR, f"{slug}.jpg")

        if not os.path.exists(image_path):
            print(f"⚠ Image not found for: {slug}")
            continue

        with open(image_path, 'rb') as image_file:
            product = Product(
                name=name,
                slug=slug,
                description=f"{name} from our {cat_name} collection.",
                price=round(random.uniform(199, 1999), 2),
                category=category,
                seller=random.choice(list(sellers.values()))
            )
            product.image.save(f"{slug}.jpg", File(image_file), save=True)
            print(f"✔ Created: {product.name} ({product.slug})")
