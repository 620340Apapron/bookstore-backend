
import sqlite3

def save_to_database(books):
    conn = sqlite3.connect("../books.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            link TEXT
        )
    """)
    for book in books:
        cursor.execute("""
            INSERT INTO books (title, price, link)
            VALUES (?, ?, ?)
        """, (book["title"], book["price"], book["link"]))
    conn.commit()
    conn.close()
