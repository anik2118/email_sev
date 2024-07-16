from flask import Flask, send_file, request
from tinydb import TinyDB, Query
from datetime import datetime
import os

app = Flask(__name__)

# Initialize TinyDB
db = TinyDB('email_tracker_db.json')
email_logs_table = db.table('email_logs')

# Initialize count from TinyDB
def get_initial_count():
    return len(email_logs_table)

count = get_initial_count()
print(f"Current count: {count}")

# Endpoint for serving the tracking pixel
@app.route('/user/<username>', methods=['GET'])
def my_function(username):
    global count
    email = request.args.get(username)
    print(email)
    print(username)
    spy_meme = "tracker.png"
    
    # Increment the count and log the event in TinyDB
    count += 1
    email_logs_table.insert({
        "email": email,
        "action": "opened",
        "timestamp": str(datetime.utcnow())
    })
    print(f"count _value {count}")
    
    return send_file(spy_meme, mimetype="image/gif")

# Endpoint for fetching the current count
@app.route('/fetch_data')
def fetch_data():
    count = get_initial_count()
    return str(count)

if __name__ == '__main__':
    app.run(debug=True)