#!/usr/bin/python3
"""flask applications method.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: stdout 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """output Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
