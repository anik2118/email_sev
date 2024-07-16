from flask import Flask, send_file

with open('no_of_email.txt', 'r') as file:
    count = int(file.read().strip())  # Convert to int and strip whitespace
    print(f"Current count: {count}")
app = Flask(__name__)

# Endpoint for serving the tracking pixel
@app.route('/')
def my_function():
    global count
    spy_meme = "tracker.png"
    count += 1
    return send_file(spy_meme, mimetype="image/gif")

# Endpoint for fetching the current count
@app.route('/fetch_data')
def fetch_data():
    return str(count)


