from flask import Flask, send_file, request
from tinydb import TinyDB, Query
from datetime import datetime

app = Flask(__name__)

# Initialize TinyDB
db = TinyDB('email_tracker_db.json')
email_logs_table = db.table('email_logs')

# Initialize count from TinyDB
def get_initial_count():
    return len(email_logs_table)

def get_email_addre():
    query = Query()
    return email_logs_table.search(query.email_holder )

count = get_initial_count()
print(f"Current count: {count}")
@app.route("/")
def hello():
    return "Hello, World!"
# Endpoint for serving the tracking pixel
@app.route('/user/<username>', methods=['GET'])
def my_function(username):
    global count
    print(f"The email holder opened the mail:{username}")
    spy_meme = "tracker.png"

    # Increment the count and log the event in TinyDB
    count += 1
    email_logs_table.insert({
        "email holder": username,
        "action": "opened",
        "timestamp": str(datetime.utcnow())
    })
    print(f"count _value {count}")
    
    return send_file(spy_meme, mimetype="image/gif")

# Endpoint for fetching the current count
@app.route('/fetch_data')
def fetch_data():
    count = get_initial_count()
    username=get_email_addre()
    return str(count),username


    