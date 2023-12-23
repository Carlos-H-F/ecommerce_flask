from flask import Flask

app = Flask(__name__)

@app.route('/')
def page_home():
    return "<h3>The King is back</h3>"