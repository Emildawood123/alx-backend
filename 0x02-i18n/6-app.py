#!/usr/bin/env python3
"""6-app.py"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get_user method"""
    login_as = request.args.get('login_as')
    if login_as and int(login_as) in users:
        return users[int(login_as)]
    else:
        return None


@app.before_request
def before_request():
    """before_request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get_locale method"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    login_as = request.args.get('login_as')
    if login_as and int(login_as) in users:
        return g.user["locale"]
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def hello():
    """hello method"""
    username = None
    login_as = request.args.get('login_as')
    if login_as and int(login_as) in users:
        username = g.user["name"]
    return render_template("5-index.html", username=username)

