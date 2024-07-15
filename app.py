from flask import Flask, send_file, request
count=0
app = Flask(__name__)
to=""
# Serve a default page. This function is not required. Serving up a spy.gif for the homepage.
@app.route('/')
def my_function():
    global count,to
    to = request.args.get('to')
    spy_meme = "tracker.png"
    count+=1
    return send_file(spy_meme, mimetype="image/gif")

@app.route('/fetch_data')
def fetch_data():   
    return str(count)


