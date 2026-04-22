import sqlite3
import random
from datetime import datetime, timedelta

def create_connection():
    return sqlite3.connect("data/sap_mock.db")

def create_tables(conn):
    cursor = conn.cursor()

    cursor.executescript("""
    DROP TABLE IF EXISTS BusinessPartner;
    DROP TABLE IF EXISTS SalesOrder;
    DROP TABLE IF EXISTS SalesOrderItem;
    DROP TABLE IF EXISTS Product;

    CREATE TABLE BusinessPartner (
        BP_ID INTEGER PRIMARY KEY,
        BP_Name TEXT,
        Region TEXT,
        Industry TEXT
    );

    CREATE TABLE Product (
        Product_ID INTEGER PRIMARY KEY,
        Product_Name TEXT,
        Category TEXT,
        Price REAL
    );

    CREATE TABLE SalesOrder (
        SO_ID INTEGER PRIMARY KEY,
        BP_ID INTEGER,
        Order_Date DATE,
        Total_Amount REAL,
        Currency TEXT,
        FOREIGN KEY (BP_ID) REFERENCES BusinessPartner(BP_ID)
    );

    CREATE TABLE SalesOrderItem (
        Item_ID INTEGER PRIMARY KEY,
        SO_ID INTEGER,
        Product_ID INTEGER,
        Quantity INTEGER,
        Net_Amount REAL,
        FOREIGN KEY (SO_ID) REFERENCES SalesOrder(SO_ID),
        FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
    );
    """)

    conn.commit()

def seed_data(conn):
    cursor = conn.cursor()

    regions = ["India", "US", "Germany"]
    industries = ["Retail", "Manufacturing", "IT"]

    # Business Partners
    for i in range(1, 21):
        cursor.execute(
            "INSERT INTO BusinessPartner VALUES (?, ?, ?, ?)",
            (i, f"Customer_{i}", random.choice(regions), random.choice(industries))
        )

    # Products
    for i in range(1, 51):
        cursor.execute(
            "INSERT INTO Product VALUES (?, ?, ?, ?)",
            (i, f"Product_{i}", "Category_A", random.randint(100, 1000))
        )

    # Orders + Items
    for i in range(1, 101):
        date = datetime.now() - timedelta(days=random.randint(0, 180))
        bp_id = random.randint(1, 20)

        total = random.randint(1000, 50000)

        cursor.execute(
            "INSERT INTO SalesOrder VALUES (?, ?, ?, ?, ?)",
            (i, bp_id, date.strftime("%Y-%m-%d"), total, "INR")
        )

        # Add items per order
        for _ in range(random.randint(1, 5)):
            product_id = random.randint(1, 50)
            qty = random.randint(1, 10)
            net = qty * random.randint(100, 1000)

            cursor.execute(
                "INSERT INTO SalesOrderItem (SO_ID, Product_ID, Quantity, Net_Amount) VALUES (?, ?, ?, ?)",
                (i, product_id, qty, net)
            )

    conn.commit()

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    seed_data(conn)
    conn.close()

    print("Database created and seeded successfully!")