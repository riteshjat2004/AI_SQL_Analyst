from sqlalchemy import text
from src.database.connection import engine

with engine.connect() as connection:

    result = connection.execute(
        text("""
        SELECT
            product_name,
            category,
            price
        FROM products
        LIMIT 5;
        """)
    )

    print("\nProducts\n")

    for row in result:
        print(row)