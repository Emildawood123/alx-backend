#!/usr/bin/env python3
"""2-app.py"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


@babel.localeselector
def get_locale():
    """get_locale method"""
    return request.accept_languages.best_match()


@app.route("/")
def hello():
    """hello method"""
    return render_template("2-index.html")
