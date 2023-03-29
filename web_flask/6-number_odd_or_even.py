#!/usr/bin/python3
"""Start Flask application"""
from flask import Flask, render_template

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


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_iscool(text='is cool'):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_oddeven(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html',
                               n=n,
                               even_or_odd='even' if n % 2 == 0 else 'odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
