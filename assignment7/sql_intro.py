# Task 1: Create a New SQLite Database
import sqlite3

# Try to connect to a new database
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database is created and connected successfully.")
except sqlite3.Error as e:
    print("Database connection failed:", e)

# Task 2: Define Database Structure

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")  # Make sure foreign keys are valid
        cursor = conn.cursor()

        # Create Publishers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        # Create Magazines table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)

        # Create Subscribers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        # Create Subscriptions table (join table)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
        )
        """)

        print("Tables created successfully.")
except sqlite3.Error as e:
    print("Error creating tables:", e)

# Task 3: Populate Tables with Data

# Functions to insert data safely
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    try:
        cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        publisher = cursor.fetchone()
        if publisher:
            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher[0]))
        else:
            print(f"Publisher '{publisher_name}' not found.")
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        else:
            print(f"Subscriber '{name}' at '{address}' already exists.")
    except sqlite3.Error as e:
        print("Error inserting subscriber:", e)

def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
    try:
        # Find subscriber_id
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
        subscriber = cursor.fetchone()
        # Find magazine_id
        cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine = cursor.fetchone()

        if subscriber and magazine:
            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                           (subscriber[0], magazine[0], expiration_date))
        else:
            print(f"Subscription creation failed for '{subscriber_name}' and '{magazine_name}'.")
    except sqlite3.Error as e:
        print("Error inserting subscription:", e)

# Insert data
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Add Publishers
        add_publisher(cursor, "Nature Press")
        add_publisher(cursor, "Tech Monthly")
        add_publisher(cursor, "Health Today")

        # Add Magazines
        add_magazine(cursor, "Nature World", "Nature Press")
        add_magazine(cursor, "Techie Times", "Tech Monthly")
        add_magazine(cursor, "Wellness Weekly", "Health Today")

        # Add Subscribers
        add_subscriber(cursor, "Alice Smith", "123 Elm St")
        add_subscriber(cursor, "Bob Johnson", "456 Oak St")
        add_subscriber(cursor, "Charlie Rose", "789 Pine St")

        # Add Subscriptions
        add_subscription(cursor, "Alice Smith", "Nature World", "2026-01-01")
        add_subscription(cursor, "Alice Smith", "Techie Times", "2026-03-15")
        add_subscription(cursor, "Bob Johnson", "Wellness Weekly", "2025-12-31")

        conn.commit()
        print("Sample data inserted successfully.")
except sqlite3.Error as e:
    print("Error inserting data:", e)

# Task 4: Write SQL Queries

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()

        # Retrieve all subscribers
        print("\nSubscribers:")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)

        # Retrieve all magazines ordered by name
        print("\nMagazines ordered by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        for row in cursor.fetchall():
            print(row)

        # Retrieve magazines for a specific publisher (Example: 'Nature Press')
        print("\nMagazines from Nature Press:")
        cursor.execute("""
        SELECT magazines.name
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = 'Nature Press'
        """)
        for row in cursor.fetchall():
            print(row)

except sqlite3.Error as e:
    print("Error with queries:", e)



