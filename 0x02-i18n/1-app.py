#!/usr/bin/env python3
"""1-app.py"""
from flask import Flask
from flask_babel import Babel
import os
import dates


class Config:
    """Cofig class"""
    def __init__(self):
        self.LANGUAGES = ["en", "fr"]


os.environ['LANG'] = Config.LANGUAGES[0]
date.DEFAULT_TIMEZONE = 'UTC'

bable = Locale.default()
