from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/books", methods=["GET"])
def get_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, publisher, price FROM books")
    books = [
        {"title": row[0], "author": row[1], "publisher": row[2], "price": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)
