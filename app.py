from flask import Flask, send_file

count = 0
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


