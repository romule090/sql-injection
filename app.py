from flask import Flask, request
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('database.db')

def create_tables():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    db.commit()

@app.route('/search')
def search():
    query = request.args.get('query')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '" + query + "'")
    results = cursor.fetchall()
    return str(results)

if __name__ == '__main__':
    create_tables()
    app.run()
