#!/usr/bin/env python3
"""1-app.py"""
import os
from flask import Flask
from babel import dates, Locale


class Config:
    """Cofig class"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)

os.environ['LANG'] = Config.LANGUAGES[0]
dates.DEFAULT_TIMEZONE = "UTC"

babel = Locale.default()
