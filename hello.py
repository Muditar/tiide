from flask import flask

myapp = flask(_name_)

@myapp.route("/")
def hello():
    return "Hello World"

@myapp.route("/tiide")
def tiide():
    return "Welcome to TIIDE World"
