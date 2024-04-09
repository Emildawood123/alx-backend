#!/usr/bin/env python3
"""4-app.py"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get_locale method"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def hello():
    """hello method"""
    return render_template("4-index.html")


if __name__ == '__main__':
    app.run(debug=True)
