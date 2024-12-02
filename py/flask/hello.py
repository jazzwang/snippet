from flask import Flask
from flask import Request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pet", methods=["GET", "POST"])
def add_pet():
    return "<p>Add pet</p>"