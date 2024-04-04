#!/usr/bin/python3
"""starts a web flask applicaton """
from flask import Flask


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
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
