import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta

fake = Faker("en_IN")
random.seed(42)

# -----------------------------
# Customers
# -----------------------------

cities = [
    "Delhi",
    "Mumbai",
    "Bhopal",
    "Indore",
    "Pune",
    "Jaipur",
    "Hyderabad",
    "Ahmedabad",
    "Lucknow",
    "Bengaluru"
]

customers = []

for i in range(1, 101):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "city": random.choice(cities)
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# Products
# -----------------------------

products = [
    ("Laptop","Electronics",55000),
    ("Smartphone","Electronics",25000),
    ("Headphones","Electronics",3000),
    ("Keyboard","Electronics",1500),
    ("Mouse","Electronics",900),
    ("Monitor","Electronics",12000),
    ("Printer","Electronics",8000),
    ("Tablet","Electronics",18000),
    ("Camera","Electronics",45000),
    ("Smart Watch","Electronics",6000),

    ("Shirt","Fashion",1200),
    ("Jeans","Fashion",1800),
    ("Shoes","Fashion",3200),
    ("Jacket","Fashion",3500),
    ("Cap","Fashion",500),

    ("Mixer","Home",2500),
    ("Microwave","Home",9500),
    ("Chair","Home",2200),
    ("Table","Home",4500),
    ("Fan","Home",2800)
]

products_df = pd.DataFrame(products,
    columns=["product_name","category","price"])

products_df.insert(0,"product_id",
                   range(1,len(products_df)+1))

# -----------------------------
# Orders
# -----------------------------

orders = []

start_date = datetime(2024,1,1)

for order_id in range(1,1001):

    orders.append({
        "order_id":order_id,
        "customer_id":random.randint(1,100),
        "order_date":(
            start_date +
            timedelta(days=random.randint(0,365))
        ).date()
    })

orders_df = pd.DataFrame(orders)

# -----------------------------
# Order Items
# -----------------------------

order_items = []

item_id = 1

for order in orders:

    num_products = random.randint(1,4)

    selected = random.sample(range(1,21),num_products)

    for p in selected:

        order_items.append({

            "order_item_id":item_id,

            "order_id":order["order_id"],

            "product_id":p,

            "quantity":random.randint(1,5)

        })

        item_id += 1

order_items_df = pd.DataFrame(order_items)

# -----------------------------
# Save CSVs
# -----------------------------

customers_df.to_csv("customers.csv",index=False)
products_df.to_csv("products.csv",index=False)
orders_df.to_csv("orders.csv",index=False)
order_items_df.to_csv("order_items.csv",index=False)

print("CSV files generated successfully!")