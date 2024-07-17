from flask import Flask, send_file, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'email_tracker.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS email_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        timestamp TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

def get_initial_count():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM email_logs')
    count = cursor.fetchone()[0]
    conn.close()
    return count

init_db()
count = get_initial_count()
print(f"Current count: {count}")

@app.route("/")
def hello():
    return "Hello, World!"

# Endpoint for serving the tracking pixel
@app.route('/user/<username>', methods=['GET'])
def my_function(username):
    global count
    spy_meme = "tracker.png"
    # Increment the count and log the event in SQLite
    count += 1
    print(f'The person has opened the mail: {username}')
    print(f"Count value: {count}")

    # Log the event in SQLite
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO email_logs (username, timestamp) VALUES (?, ?)', 
                   (username, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    
    return send_file(spy_meme, mimetype="image/gif")

# Endpoint for fetching the current count
@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    count = get_initial_count()
    return str(count)

# Endpoint for fetching the usernames that accessed the tracking pixel
@app.route('/fetch_usernames', methods=['GET'])
def fetch_usernames():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM email_logs')
    logs = cursor.fetchall()
    conn.close()
    usernames = [log[0] for log in logs]
    return jsonify(usernames)

