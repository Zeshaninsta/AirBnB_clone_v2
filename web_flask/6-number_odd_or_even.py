#!/usr/bin/python3
"""starts a web flask applicaton """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """starts default route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """starts /hbnb route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    return "C {}".format(text)


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text):
    """return python followed by a text form a user """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return if a given input is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """displays html page only if a given number is integer """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """"checks if a number is even or odd and returns accordingly """
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
