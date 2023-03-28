#!/usr/bin/python3
"""Start Flask application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_olleh():
    return 'HBNB'

@app.route('/c/')
@app.route('/c/<text>', strict_slashes=False)
def c_is_confuse(text):
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
