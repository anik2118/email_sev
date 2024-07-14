from flask import Flask, send_file, request
import datetime
import urllib.request
count=0
app = Flask(__name__)

# Serve a default page. This function is not required. Serving up a spy.gif for the homepage.
@app.route('/')

def my_function():
    global count
    spy_meme = "tracker.png"
    count+=1
    return send_file(spy_meme, mimetype="image/gif")

@app.route('/fetch_data')
def fetch_data():   
    return count

@app.route('/image')
def my_spy_pixel():
    # File path and name for 1 x 1 pixel. Must be an absolute path to pixel.
    filename = "logo.png"

    # Log the User-Agent String.
    user_agent = request.headers.get('User-Agent')

    # Get the current time of request and format time into readable format.
    current_time = datetime.datetime.now()
    timestamp = datetime.datetime.strftime(current_time, "%Y-%m-%d %H:%M:%S")

    # Log the IP address of requester.
    get_ip = request.remote_addr

    # Lookup Geolocation of IP Address.
    with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ get_ip) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")

    # Add User-Agent, Timestamp, and IP Address + Geolocation information to dictionary.
    log_entry = f"Email Opened:\nTimestamp: {timestamp}\nUser Agent: {user_agent}\nIP Address: {data}\n"

    # Write log to hardcoded path. Must be an absolute path to the log file.
    with open('testing_purposes.txt', 'a') as f:
        f.write(log_entry)

    # Serve a transparent pixel image when navigating to .../image URL. "image/png" displays the image in PNG format.
    return send_file(filename, mimetype="image/png")


if __name__ == '__main__':
    app.run()