from flask import Flask, send_file, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://anikghoshr123:iSOpoAz1cibNO3we@emailsender0.ciaq5yv.mongodb.net/")  # Replace with your MongoDB connection string
db = client["email_tracker_db"]
email_logs_collection = db["email_logs"]

# Initialize count from MongoDB
def get_initial_count():
    return email_logs_collection.count_documents({})

count = get_initial_count()
print(f"Current count: {count}")

# Endpoint for serving the tracking pixel
@app.route('/')
def my_function():
    global count
    email = request.args.get('email')
    spy_meme = "tracker.png"
    
    # Increment the count and log the event in MongoDB
    count += 1
    email_logs_collection.insert_one({
        "email": email,
        "action": "opened",
        "timestamp": datetime.utcnow()
    })
    print(f"count _value {count}")
    
    return send_file(spy_meme, mimetype="image/gif")

# Endpoint for fetching the current count
@app.route('/fetch_data')
def fetch_data():
    count = get_initial_count()
    return str(count)

