from flask import flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello World"

@myapp.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
