import sqlite3

#Task 3
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"{name} with already in the database.")
def add_subscribers(cursor, name,address):
    try:
        cursor.execute("INSERT INTO subscribers (subscriber_name,subscriber_address) VALUES (?,?)", (name,address))
    except sqlite3.IntegrityError:
        print(f"{name} with {address} is already in the database.")
def add_magazine(cursor, name,publisher):
    cursor.execute("SELECT * FROM publishers WHERE publisher_name = ?", (publisher,))
    results = cursor.fetchall()
    if len(results) > 0:
        publisher_id = results[0][0]
    else:
        print(f"There was no publisher named {publisher}.")
    try:
        cursor.execute("INSERT INTO magazines (magazine_name,publisher_id) VALUES (?,?)", (name,publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} with {publisher_id}is already in the database.")
def add_subscriptions(cursor, subscriber_name,subscriber_address,magazine, exp_date):
    cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ? AND subscriber_address = ?", (subscriber_name,subscriber_address))
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"There was no subscriber named {subscriber_name} with {subscriber_address} address.")
    cursor.execute("SELECT * FROM magazines WHERE magazine_name = ?", (magazine,))
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"There was no magazine named {magazine}.")
    try:
        cursor.execute("INSERT INTO subscriptions (subscriber_id,magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id,magazine_id, exp_date))
    except sqlite3.IntegrityError:
        print(f"Supscription from {magazine} for {subscriber_name} with address {subscriber_address} which expires on {exp_date} is already in the database.")


#Task 1
try:
    with  sqlite3.connect("../db/magazines.db") as conn: 
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        #Task 2
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            publisher_name TEXT NOT NULL UNIQUE
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            magazine_name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            subscriber_address TEXT NOT NULL,
            UNIQUE(subscriber_name, subscriber_address)
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
            UNIQUE(subscriber_id, magazine_id)
        )
        """)
except sqlite3.Error as e:
    print("Error:", e)


add_publisher(cursor, 'Penguin Random House')
add_publisher(cursor, 'HarperCollins')
add_publisher(cursor, 'Macmillan Publishers')
add_subscribers(cursor, 'Elly McMorris','222 City Dr')
add_subscribers(cursor, 'Li Smith','232 Hill St')
add_subscribers(cursor, 'Li Smith','111 Hill St')
add_subscribers(cursor, 'Le Smith','111 Hill St')
add_magazine(cursor, 'Time','HarperCollins')
add_magazine(cursor, 'Vogue','Penguin Random House')
add_magazine(cursor, 'National Geographic','Macmillan Publishers')
add_magazine(cursor, 'ABB','Penguin Random House')
add_subscriptions(cursor, 'Elly McMorris','222 City Dr', 'ABB','12/11/11')
add_subscriptions(cursor, 'Li Smith','232 Hill St', 'ABB','12/14/15')
add_subscriptions(cursor, 'Li Smith','232 Hill St', 'Vogue','12/14/25')
add_subscriptions(cursor, 'Le Smith','111 Hill St', 'National Geographic','03/14/24')
add_subscriptions(cursor, 'Li Smith','111 Hill St', 'Time','01/07/22')
conn.commit()

#TASK 4
cursor.execute("SELECT * FROM subscribers;")
subscribers_inf = cursor.fetchall()
print(subscribers_inf)

cursor.execute("SELECT * FROM magazines ORDER BY magazine_name;")
magazine_byN = cursor.fetchall()
print(magazine_byN)

cursor.execute("SELECT * FROM magazines JOIN publishers ON  magazines.publisher_id = publishers.publisher_id WHERE publishers.publisher_name = 'Penguin Random House';")
magazine_publ = cursor.fetchall()
print(magazine_publ)
conn.close()